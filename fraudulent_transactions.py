"""Problema 2:

Escribe una función que tome una Lista/Arreglo 2D de transacciones 
y devuelva una lista de IDs de transacciones que son fraudulentas. 
Cualquier transacción mayor o igual a 10000 se considera fraudulenta. 
Cualquier transacción de la misma tarjeta de crédito en una ciudad 
diferente dentro de los 30 minutos también se considera fraudulenta.

Entrada: Una Lista/Arreglo 2D de transacciones, donde cada registro 
de transacción tiene un ID de transacción (entero), ID de tarjeta de 
crédito (entero), cantidad de transacción (doble), ciudad (cadena) y 
tiempo en minutos (entero). Puedes asumir que todas las transacciones 
ocurren el mismo día.
"""

from typing import List, Tuple


def find_fraudulent_transactions(
    transactions: List[Tuple[int, int, float, str, int]]
) -> List[int]:
    """Identify fraudulent transactions from a list of credit card transactions.

    A transaction is considered fraudulent if:
    1. The transaction amount is 10,000 or higher.
    2. It occurs with the same credit card in a different city within 30 minutes
    of a previous transaction.

    Args:
        transactions: List of transactions. Each transaction contains:
            - Transaction ID (int)
            - Credit card ID (int)
            - Transaction amount (float)
            - City (str)
            - Transaction time in minutes since start of the day (int)

    Returns:
        List of transaction IDs that are considered fraudulent.
    """

    # Dictionary to store transactions histort by card
    # It will have the following strucure:
    # {
    #   card1_id: [
    #       ("transaction1_city", "transaction1_time"),
    #       ("transaction2_city", "transaction2_time"),
    #   ],
    #   ...
    # }
    card_transactions = dict()

    # List to store the IDs of fraudulent transactions
    fraudulent_ids = []

    for transaction in transactions:
        transaction_id, card_id, amount, city, time = transaction

        # Check if the transaction amount is fraudulent
        if amount >= 10000:
            fraudulent_ids.append(transaction_id)

        if card_id in card_transactions:
            # Iterate over the card history
            for previous_city, previous_time in card_transactions[card_id]:
                # Check for fraudulent city change within 30 minutes
                if city != previous_city and abs(time - previous_time) <= 30:
                    fraudulent_ids.append(transaction_id)
                    break

        # Create a new empty history for the current card
        # if not exists in card_transactions
        if card_id not in card_transactions:
            card_transactions[card_id] = []

        # Add the current transaction to the card history
        card_transactions[card_id].append((city, time))

    return list(set(fraudulent_ids))  # Remove duplicates
