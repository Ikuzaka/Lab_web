import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Product
from login.models import MyUser


class FavoriteConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']

        # Проверяем, авторизован ли пользователь
        if self.user.is_authenticated and isinstance(self.user, MyUser):
            self.group_name = f'user_{self.user.id}_favorites'

            # Присоединяемся к группе пользователя
            await self.channel_layer.group_add(
                self.group_name,
                self.channel_name
            )
            await self.accept()

            # Отправляем приветственное сообщение
            await self.send(json.dumps({
                'type': 'connection_established',
                'message': 'WebSocket connected successfully'
            }))


    async def disconnect(self, close_code):
        if hasattr(self, 'group_name'):
            await self.channel_layer.group_discard(
                self.group_name,
                self.channel_name
            )

    async def receive(self, text_data):
        if not self.user.is_authenticated:
            await self.send(json.dumps({
                'error': 'Please login first',
                'redirect': '/login/'
            }))
            return

        try:
            text_data_json = json.loads(text_data)
            product_id = text_data_json.get('product_id')

            if product_id:
                # Переключаем статус избранного
                result = await self.toggle_favorite(product_id)

                if result.get('success'):
                    # Отправляем обновление текущему пользователю
                    await self.send(json.dumps(result))

                    # Отправляем обновление всем в группе пользователя
                    # (полезно если у пользователя открыто несколько вкладок)
                    await self.channel_layer.group_send(
                        self.group_name,
                        {
                            'type': 'favorite_update',
                            'data': result
                        }
                    )
                else:
                    await self.send(json.dumps(result))

        except json.JSONDecodeError:
            await self.send(json.dumps({
                'error': 'Invalid JSON format'
            }))
        except Exception as e:
            await self.send(json.dumps({
                'error': f'Server error: {str(e)}'
            }))

    async def favorite_update(self, event):
        # Отправляем обновление всем клиентам в группе
        await self.send(json.dumps(event['data']))

    @database_sync_to_async
    def toggle_favorite(self, product_id):
        try:
            product = Product.objects.get(id=product_id)

            # Проверяем, есть ли продукт в избранном у пользователя
            if product.favorite_by.filter(id=self.user.id).exists():
                # Удаляем из избранного
                product.favorite_by.remove(self.user)
                is_favorited = False
                message = 'Product removed from favorites'
            else:
                # Добавляем в избранное
                product.favorite_by.add(self.user)
                is_favorited = True
                message = 'Product added to favorites'

            return {
                'success': True,
                'product_id': product_id,
                'favorites_count': product.favorites,
                'is_favorited': is_favorited,
                'message': message
            }

        except Product.DoesNotExist:
            return {
                'success': False,
                'error': 'Product not found',
                'product_id': product_id
            }
        except Exception as e:
            return {
                'success': False,
                'error': f'Database error: {str(e)}',
                'product_id': product_id
            }