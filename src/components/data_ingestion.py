import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import kagglehub

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation, DataTransformationConfig

from src.components.model_trainer import ModelTrainer, ModelTrainerConfig
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            path = kagglehub.dataset_download("kunwarakash/chennai-housing-sales-price",path="Chennai houseing sale.csv")
            df = pd.read_csv(path)
            d=df.copy()
            d.AREA=d.AREA.str.lower()
            d.SALE_COND=d.SALE_COND.str.lower()
            d.PARK_FACIL=d.PARK_FACIL.str.lower()
            d.BUILDTYPE=d.BUILDTYPE.str.lower()
            d.UTILITY_AVAIL=d.UTILITY_AVAIL.str.lower()
            d.STREET=d.STREET.str.lower()
            d.replace({'AREA':{'velchery':'velachery',
                       'kknagar':'kk nagar',
                       'tnagar':'t nagar',
                       'chormpet':'chrompet',
                       'chrompt':'chrompet',
                       'chrmpet':'chrompet',
                       'ana nagar':'anna nagar',
                       'ann nagar':'anna nagar',
                       'karapakam':'karapakkam',
                       'adyr':'adyar'},
           'SALE_COND':{'ab normal':'abnormal','partiall':'partial','adj land':'adjland','normal sale':'normalsale'},
           'PARK_FACIL':{'no':0,'noo':0,'yes':1},
           'BUILDTYPE':{'comercial':'commercial','others':'other'},
           'UTILITY_AVAIL':{'all pub':'allpub','nosewr ':'nosewr', 'nosewa':'nosewr'},
           'STREET':{'no access':'noaccess','pavd':'paved'}},inplace=True)

            # Correcting Date columnd from object to daterime format
            d.DATE_SALE = pd.to_datetime(d.DATE_SALE, format='%d-%m-%Y')
            d.DATE_BUILD = pd.to_datetime(d.DATE_BUILD, format='%d-%m-%Y')

            # Creating PROPERTY_AGE column which deternine how old the property id
            d['PROPERTY_AGE'] = pd.DatetimeIndex(d.DATE_SALE).year - pd.DatetimeIndex(d.DATE_BUILD).year

            
            d = d.reindex(columns = [ 'AREA', 'SALE_COND', 'PARK_FACIL',
       'BUILDTYPE', 'UTILITY_AVAIL', 'STREET', 'MZZONE', 'PROPERTY_AGE',
       'INT_SQFT', 'DIST_MAINROAD', 'N_BEDROOM','N_BATHROOM', 'N_ROOM','SALES_PRICE'])

            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            d.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(d,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))


