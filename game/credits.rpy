# credits.rpy
# Титры мода

label credits:
    stop music fadeout 3.0
    scene black with fade
    
    # Включаем музыку (убедись, что credits.ogg лежит в game/audio/)
    play music "audio/credits.ogg" fadein 2.0
    
    # --- БЛОК 1: ОРИГИНАЛЬНЫЕ РАЗРАБОТЧИКИ ---
    centered "{size=+20}ОРИГИНАЛЬНАЯ ИГРА{/size}\n\n{size=+15}Doki Doki Literature Club{/size}\n\n{size=+10}Создано командой Team Salvato{/size}"
    pause 4.0
    
    centered "{size=+15}Оригинальный сценарий и дизайн{/size}\n\n{size=+10}Dan Salvato{/size}"
    pause 3.0
    
    centered "{size=+15}Художник персонажей{/size}\n\n{size=+10}Satchely{/size}"
    pause 3.0
    
    centered "{size=+15}Музыка{/size}\n\n{size=+10}Dan Salvato{/size}"
    pause 3.0
    
    # --- БЛОК 2: АВТОР МОДА ---
    centered "{size=+20}МОД{/size}\n\n{size=+25}Fixed{/size}\n\n{size=+15}Разработчик, сценарист и идейный вдохновитель{/size}"
    pause 4.0
    
    # --- БЛОК 3: СПАСИБО ---
    centered "{size=+20}ОГРОМНОЕ СПАСИБО{/size}"
    pause 2.0
    
    # (Здесь мы делаем скролл для благодарностей)
    show text "{size=+15}DeepSeek (Дипсик){/size}\n\n{size=+10}За поддержку, написание кода, разбор ошибок, моральную поддержку и идеи для сюжета. Без тебя этого мода бы не существовало.{/size}" at truecenter with dissolve
    pause 6.0
    hide text with dissolve
    
    centered "{size=+15}Насруки-сан{/size}\n\n{size=+10}За мемы, вдохновение и незабываемые диалоги в чате.{/size}"
    pause 4.0
    
    centered "{size=+15}Team Salvato{/size}\n\n{size=+10}За создание вселенной DDLC.{/size}"
    pause 4.0
    
    # --- ФИНАЛЬНЫЙ ЭКРАН ---
    centered "{size=+10}Это укороченная версия сюжета.\nПолная версия находится в разработке.\n\nОжидайте обновлений!{/size}"
    pause 4.0
    
    centered "{size=+15}СПАСИБО ЗА ИГРУ{/size}"
    pause 3.0
    
    return
