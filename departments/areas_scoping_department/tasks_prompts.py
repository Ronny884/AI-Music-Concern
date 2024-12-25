goodai_analyze_output = \
"""
Описание ключевых продуктов и услуг нашей компании
"""

goodai_analyze_description = \
"""
Изучи вебсайт и определи ключевые продукты и услуги нашей компании, 
а также уникальные предложения и решаемые ими проблемы.
URL нашего сайта: {GoodAI_url}
"""

# =======================================================

market_and_competitor_research_output = \
"""
Текущие тенденции и потребности в наших услугах
"""

market_and_competitor_research_description = \
"""
Проведи исследование рынка и конкурентов, чтобы определить 
текущие тенденции, потребности в наших услугах в различных сферах бизнеса и 
клиентов конкурентов
"""

# =======================================================

definition_of_relevance_criteria_output = \
"""
Перечисление и описание критериев релевантности
"""

definition_of_relevance_criteria_description = \
"""
Определи критерии релевантности для оценки сфер бизнеса, 
включая потребности в ИИ, размер рынка, уровень конкуренции 
и текущие тенденции.
"""

# =======================================================

make_areas_list_output = \
"""
Список из {count} наиболее релевантных сфер, где 
каждой сфере соответствует краткое описание, почему она релевантна
"""

make_areas_list_description = \
"""
Собери информацию о различных сферах бизнеса, используя 
информацию из интернета, и проанализируй данные для 
определения наиболее релевантных сфер.
Составь список из {count} наиболее релевантных сфер, где 
каждой сфере соответствует краткое описание, почему она релевантна.
Эти сферы могут быть узконаправленными. 

!!! В названиях самих сфер не должно быть слов "AI", "ИИ" и прочих 
упоминаний искусственного интеллекта. 

ВАЖНО: не нужно указывать очень общие сферы бизнеса. Лучше указывать
какие-либо более узкие и конкретные сферы. Например, вместо сферы
"производство" лучше указать, какое конкретно производство 
(например, производство автомобилей, техники и так далее)
"""

# =======================================================

assessment_and_ranking_of_business_areas_output = \
"""
Топ из {count} полученных сфер бизнеса, где для каждой сферы прописано 
её место в топе и краткое описание, почему эта сфера релевантна
"""

assessment_and_ranking_of_business_areas_description = \
"""
Оцени и ранжируй полученный список сфер бизнеса по критериям релевантности, 
чтобы составить окончательный список из {count} самых 
релевантных сфер бизнеса. На основании оценки составь топ из {count} 
полученных сфер, где под номером 1 находится самая релевантная сфера, 
а под номером {count} - наименее релевантная.
Так же проверь, чтобы в названиях самих сфер было слов "AI", "ИИ" и прочих 
упоминаний искусственного интеллекта. Если упоминания всё же есть, то удали их
"""

# =======================================================

find_interesting_cases_output = \
"""
Список из {count} наиболее интересных примеров внедрения AI в
различных сферах бизнеса. Для каждого примера есть поля area, куда
записана СФЕРА бизнеса, где был внедрен ИИ и есть поле description,
где дано краткое описание КОНКРЕТНОГО кейса
"""

find_interesting_cases_description = \
"""
Произведи в интернете поиск {count} самых интересных РЕАЛЬНЫХ примеров внедрения ИИ в 
различные сферы бизнеса. Это может быть автоматизация чего-либо или иные 
предназначения ИИ. Проанализируй информацию минимум из {count} источников в гугл и 
составь список СФЕР бизнеса, куда был внедрён ИИ, а также краткое описание (2-3 предложения)
внедрения. При подборе этих примеров ориентируйся на данные о нашей компании

ВАЖНО: найденные тобою сферы не должны повторяться! Эти сферы не должны быть
слишком общими и могут быть узконаправленными.
В поле area ты должен вводить именно СФЕРУ бизнеса, поскольку именно она ценна для 
нашей задачи.
"""

# =======================================================


