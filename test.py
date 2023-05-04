from src.kafka_logger import logger

def multiply(a, b):
    logger.logging.info(f"Multiplication of two numbers: {a * b}")
    return a * b

def divide(a, b):
    try:
        logger.logging.info("Division of two numbers")
        div = a/b
        logger.logging.info(f"Division of {a} and {b} is {div}")
        return div
    except Exception as e:
        logger.logging.error(f"Error is {e}")
        raise e

if __name__ == "__main__":
    divide(2, 0)