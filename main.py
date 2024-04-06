from data_ingestion.data_ingestion import retrive_key
from data_transformation.data_transformation import apply_transformation
from db_connection import connect_to_database, create_table, insert_data, close_connection
import logging

def main():
    
    ## SQLite connection
    conn = connect_to_database()

    # Create the table if it doesn't exist
    create_table(conn)


    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='app.log', filemode='w')

    # Log start of the program
    logging.info('Starting the program...')

    ## 

    # api
    api_key = '5782baf9-b3d1-4670-8c61-11dacda86b6d'

    logging.info('Retrieving data from the API...')
    crypto_data = retrive_key(api_key)

    # If data retrieval is successful, proceed with transformations
    if crypto_data:
        logging.info('Data retrieval successful.')
        # Assuming bitcoin_price is obtained separately, either from the API or another source
        bitcoin_price = 66042.85516079019  # Example value for demonstration

        # Apply transformations to the retrieved data
        transformed_data = apply_transformation(crypto_data, bitcoin_price)

        # Insert transformed data into the database
        insert_data(conn, transformed_data)


        # Print or further process the transformed data
        for item in transformed_data:
            print(item)
    else:
        logging.error('Error: Unable to retrieve data from the API.')
        
    logging.info('Exiting the program...')
    close_connection(conn)
    

if __name__ == "__main__":
    main()
