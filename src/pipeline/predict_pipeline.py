import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,feature):
        try:
            model_path = 'artifacts/model.pkl'
            preprocessor_path = 'artifacts/preprocessor.pkl'
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled = preprocessor.transform(feature)
            preds = model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self,
                 AREA:str,
                 SALE_COND:str,
                 PARK_FACIL:str,
                 BUILDTYPE:str,
                 UTILITY_AVAIL:str,
                 STREET: str,
                 MZZONE:str,
                 PROPERTY_AGE:int,
                 INT_SQFT:int,
                 N_BEDROOM:int,
                 N_BATHROOM:int,
                 N_ROOM:int):
        
        self.AREA=AREA
        self.SALE_COND=SALE_COND
        self.PARK_FACIL=PARK_FACIL
        self.BUILDTYPE=BUILDTYPE
        self.UTILITY_AVAIL=UTILITY_AVAIL
        self.STREET=STREET
        self.MZZONE=MZZONE
        self.PROPERTY_AGE=PROPERTY_AGE
        self.INT_SQFT=INT_SQFT
        self.N_BEDROOM=N_BEDROOM
        self.N_BATHROOM=N_BATHROOM
        self.N_ROOM=N_ROOM


    def get_data_as_data_frame(self):
            try:
                custom_data_input_dict = {
                    "AREA":[self.AREA],
                    "SALE_COND":[self.SALE_COND],
                    "PARK_FACIL":[self.PARK_FACIL],
                    "BUILDTYPE":[self.BUILDTYPE],
                    "UTILITY_AVAIL":[self.UTILITY_AVAIL],
                    "STREET":[self.STREET],
                    "MZZONE":[self.MZZONE],
                    "PROPERTY_AGE":[self.PROPERTY_AGE],
                    "INT_SQFT":[self.INT_SQFT],
                    "N_BEDROOM":[self.N_BEDROOM],
                    "N_BATHROOM":[self.N_BATHROOM],
                    "N_ROOM":[self.N_ROOM]
                }

                return pd.DataFrame(custom_data_input_dict)
            
            except Exception as e:
                raise CustomException(e, sys)
