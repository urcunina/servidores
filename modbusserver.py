#!/usr/bin/env python
"""
Pymodbus Synchronous Server Example
--------------------------------------------------------------------------

The synchronous server is implemented in pure python without any third
party libraries (unless you need to use the serial protocols which require
pyserial). This is helpful in constrained or old environments where using
twisted is just not feasible. What follows is an example of its use:
"""
# --------------------------------------------------------------------------- #
# import the various server implementations
# --------------------------------------------------------------------------- #
# Del OPC
from opcua import Client
from opcua import ua
import time

import threading

from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSparseDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

from pymodbus.transaction import ModbusRtuFramer, ModbusBinaryFramer
# --------------------------------------------------------------------------- #
# configure the service logging
# --------------------------------------------------------------------------- #
import logging
FORMAT = ('%(asctime)-15s %(threadName)-15s'
          ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
# FORMAT=()
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.ERROR)


VECTOR_OPC=[]



def Vector2Modbus():
    for i in range(0,len(VECTOR_OPC)):
        if VECTOR_OPC[i]==True:
            # context[0].setValues(0x0,[1,0,1,0,1,0,1])
            # context[0].setValues(1,[7])
            # print("True")
            context[0].setValues(0x0, 1, [1])
            # context[0].setValues(0x1, 1, [0])
            # context[0].setValues(0x1, 2, [1])
            # context[0].setValues(0x1, 3, [0])
            # context[0].setValues(0x1, 4, [1])
            # context[0].setValues(0x1, 5, [0])
        else:
            # context[0].setValues(0x0,[0,1,0,1,0,1,0])
            # context[0].setValues(1,[4])
            # print("false")
            context[0].setValues(0x5, 0, VECTOR_OPC)
            # context[0].setValues(0x1, 1, [0])
            # context[0].setValues(0x1, 2, [1])
            # context[0].setValues(0x1, 3, [0])
            # context[0].setValues(0x1, 4, [1])
            # context[0].setValues(0x1, 5, [0])

def Opc2Vector():
    try:
        root = client.get_root_node()    
        childrenroot=root.get_children()    
        objects=childrenroot[0].get_children()   
        CAMARA=objects[1].get_children() # En el nodo DA plugin 
        # print(CAMARA[0])
        # Leemos las señales generadas para cada cámara  CAM1  CAM42
        for i in range(0,42):
        # for i in range(0,1):
            # time.sleep(0.1)
            signals=CAMARA[i].get_children()
            # if i==0:                
                # print(signals)
                # time.sleep(20)
            for z in range(0,16):
                # time.sleep(0.1)
                # if z==0:
                    # print(signals[z])
                if signals[z].get_value()==True:
                # VECTOR_OPC.append(signals[z].get_value())
                    # print("Alarma en", i, z)
                    VECTOR_OPC.append(1)
                else:
                    VECTOR_OPC.append(0)
                # print(signals[z].get_value()) 
                # nada=0 
        # Leemos las señales generadas para cada SVR  x SVR1  SVR3  SVR4 SVR5  SVR6  SVR2
        # SRV1.TS.STAT_EQPT, 
        # SRV1.TS.AL_COMM_ERROR, 
        # SRV1.TS.IS_ACTIVE)
        SRV1=CAMARA[42].get_children()
        TS=SRV1[0].get_children()
        # print(TS[0].get_value())
        # print(TS[1].get_value())
        # print(TS[2].get_value())        
        VECTOR_OPC.append(TS[0].get_value())            
        if TS[1].get_value()==True:
            VECTOR_OPC.append(1)
        else:
            VECTOR_OPC.append(0)
            
        if TS[2].get_value()==True:
            VECTOR_OPC.append(1)
        else:
            VECTOR_OPC.append(0)   
            
        # SVR2.TS.STAT_EQPT 
        # SVR2.TS.AL_COMM_ERROR
        SRV2=CAMARA[43].get_children()
        TS=SRV2[0].get_children()
        # print(TS[0].get_value())
        # print(TS[1].get_value())
        VECTOR_OPC.append(TS[0].get_value()) 
            
        if TS[1].get_value()==True:
            VECTOR_OPC.append(1)
        else:
            VECTOR_OPC.append(0)
        
        # SVR3.TS.STAT_EQPT 
        # SVR3.TS.AL_COMM_ERROR
        SRV3=CAMARA[44].get_children()
        TS=SRV3[0].get_children()
        # print(TS[0].get_value())
        # print(TS[1].get_value())
        VECTOR_OPC.append(TS[0].get_value()) 
            
        if TS[1].get_value()==True:
            VECTOR_OPC.append(1)
        else:
            VECTOR_OPC.append(0)
        
        # SRV4.TS.STAT_EQPT
        # SRV4.TS.AL_COMM_ERROR
        SRV4=CAMARA[45].get_children()
        TS=SRV4[0].get_children()
        # print(TS[0].get_value())
        # print(TS[1].get_value())
        VECTOR_OPC.append(TS[0].get_value()) 
            
        if TS[1].get_value()==True:
            VECTOR_OPC.append(1)
        else:
            VECTOR_OPC.append(0)
        
        # SRV5.TS.STAT_EQPT
        # SRV5.TS.AL_COMM_ERROR
        SRV5=CAMARA[46].get_children()
        TS=SRV5[0].get_children()
        # print(TS[0].get_value())
        # print(TS[1].get_value())
        VECTOR_OPC.append(TS[0].get_value()) 
            
        if TS[1].get_value()==True:
            VECTOR_OPC.append(1)
        else:
            VECTOR_OPC.append(0)
        
        # SRV6.TS.STAT_EQPT
        # SRV6.TS.AL_COMM_ERROR
        SRV6=CAMARA[47].get_children()
        TS=SRV6[0].get_children()
        # print(TS)
        # print(TS[0].get_value())
        # print(TS[1].get_value())
        VECTOR_OPC.append(TS[0].get_value()) 
            
        if TS[1].get_value()==True:
            VECTOR_OPC.append(1)
        else:
            VECTOR_OPC.append(0)
        
        print(VECTOR_OPC)
        print(len(VECTOR_OPC))
        if len(VECTOR_OPC)==685:
            # print("2 MODBUS")
            # context[0].setValues(5, 0, VECTOR_OPC)  # Escribe Coil
            # context[0].setValues(3, 0, VECTOR_OPC)
            # context[1].setValues(3, 0, VECTOR_OPC)
            context[2].setValues(3, 0, VECTOR_OPC)
            # context[3].setValues(3, 0, VECTOR_OPC)

    except:  # Ya que se puede perder la conexión con el servidor realizamos esta acción
        print("Error en función OPCsoshardwareread")
        print("Reconectando...")
        time.sleep(0.1)
        try:
            client.connect()
            print("Reconectado satisfactoriamente")
        except:
            print("Error reconectando")        
        return
    
    
def run_server(context,identity):   
    StartTcpServer(context, identity=identity, address=("", 502))


if __name__ == "__main__":
    
    # Conecta con el OPC de Video
    client = Client("opc.tcp://192.168.13.240:62886/Citilog/OpcUaServer")
    conexion=0  ## Esta variable determina si hubo una conexión incial, al momento del arranque
    while(conexion==0):
        time.sleep(1)
        try:
            client.connect()
            conexion=1
            print("Conexión establecida")
            time.sleep(2)
            break
        except:
            print("No se tiene conexión con el servidor de video")            
    
    # store = ModbusSlaveContext(hr=ModbusSequentialDataBlock(0,[1]*674))    # debe ser +2   
    store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [17]*687),
    co=ModbusSequentialDataBlock(0, [17]*687),
    hr=ModbusSequentialDataBlock(0, [17]*687),
    ir=ModbusSequentialDataBlock(0, [17]*687))
    context = ModbusServerContext(slaves=store, single=True)
    
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'pymodbus'
    identity.ProductCode = 'PM'
    identity.VendorUrl = 'http://github.com/bashwork/pymodbus/'
    identity.ProductName = 'pymodbus Server'
    identity.ModelName = 'pymodbus Server'
    identity.MajorMinorRevision = '2.3.0'

    ModbusServerOnhilo=threading.Thread(target=run_server,args=(context,identity,))
    ModbusServerOnhilo.start()

while(1):
    Opc2Vector()
    # Vector2Modbus()    
    VECTOR_OPC=[]  # Resteamos lista para que se expanda
    
       # run_server()

    # print("sale")
    
    