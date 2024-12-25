# AI Music Concern

Проект на основе агентов ИИ, который выполняет следующие задачи:
- поиск сфер бизнеса по заданному описанию предполагаемо вашей компании (CrewAI)
- поиск компаний в заданном количестве, работающих в заданной сфере бизнеса и находящихся в указанной стране (CrewAI)
- для каждой найденной компании производится ресёрч в google и скрэпинг веб-сайтов в целях сбора информации о ней (Autogen, Serper, Hunter.io API)
- по найденной информации для каждой компании сочиняется песня на языке страны, где располагается компания (OpenAI API)
- сочинённая песня озвучивается с помощью одного из двух сервисов по API (TopmediAI, SunoAI)
- для каждой песни mp3 создаётся видео mp4 со сгенерированной картинкой и текстовой дорожкой (Whisper, библиотеки Pillow, moviepy)
- это видео загружается на Vimeo (Vimeo API)
- генерация текста сообщения на актуальном языке и, если необходимо, создание html для более красивого оформления письма (OpenAI API)
- на электронную почту компании, найденную спомощью hunter.io или Autogen, отправляется письмо со ссылкой на музыкальное видео (SMTP-клиент gmail)

  ## Основные технологии
  В проекте использованы передовые фреймворки для работы с агентами ИИ, такие как CrewAI и Autogen. Так же использовались соновные возможности API Chat Completions и Whisper.
  Для озвучки текста песни использовалось API TopmediAI, а так же неофициальное API SunoAI (в меньшей степени)

  ## Скриншот музыкального видео:
  <img src="https://github.com/user-attachments/assets/d99ab51a-6634-4e99-bd45-f6dc5bab9ebd" alt="Description" width="500" height="700">


