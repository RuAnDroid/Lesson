from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token="5770862184:AAENx0D9pjr0sw3nfs3k1_bEEkUccQgFmWA")
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather.IMPERIAL)


@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.find(message.text)
    resp_msg = message.text
    celsius = (weather.current.temperature - 32) / 1.8
    resp_msg = weather.location_name + "/n"
    resp_msg += f"Текущая температура:{celsius}/n"
    resp_msg += f"Состояние погоды:{weather.current.sky_text}"
    await message.answer(resp_msg)


if __name__ == '__main__':
    executor.start_polling(dp)
