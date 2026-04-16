import logging
import os

# Логду жөндөө
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

def get_user_age():
    logging.info("Жаш суроо функциясы башталды.")
    try:
        # 👉 Берем из ENV или используем input
        age_input = os.getenv("AGE")

        if age_input is None:
            age_input = input("Жашыңызды киргизиңиз: ")

        age = int(age_input)

        logging.info(f"Колдонуучу киргизген жаш: {age}")
        print(f"Рахмат! Сиздин жашыңыз: {age}")

    except ValueError:
        logging.error("Ката! Колдонуучу сан эмес маалымат киргизди.")
        print("Сураныч, бир гана сан киргизиңиз!")

    except EOFError:
        logging.error("Ката! Киргизүү жок (CI чөйрөсү).")
        print("Киргизүү табылган жок (CI).")

if __name__ == "__main__":
    logging.info("Программа ишке кирди.")
    get_user_age()
    logging.info("Программа ийгиликтүү аяктады.")