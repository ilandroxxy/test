# region import-ы
from aiogram import Bot, Dispatcher, executor, types

token = '5734914555:AAETPQsfcDp2H7XJVJfdqpnvpVeMrLLmNso'

bot = Bot(token)
dp = Dispatcher(bot)
# endregion import-ы


async def on_startup(_):
    print('Я был запущен!')


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(text=f"Привет, {message.from_user.first_name}", reply_markup=kb)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)