import io, os, os.path
import mmap
import sys

def _leer_argumentos():
    try:
        print('parametros [{}], {}'.format(len(sys.argv), sys.argv))
        _path = sys.argv[1]
        _prm_str = sys.argv[2]

        print('_path={}, _prm_str={}'.format(_path, _prm_str))
        _exec_process = 1
    except IndexError:
        _exec_process = 0

def _buscar_datos(strfind, _path):
    #_path = 'D:\\temp\\AdminCups'
    _path = _path.replace("/", "\\")
    print("Path: {}".format(_path))
    count_files = 0
    count_files_find = 0

    print(' ******************************************************* ')
    print('  inicia proceso')
    print(' ******************************************************* ')
    #print('  {}'.format(_path))
    #strfind = "908704|BETA GLUCORONIDASA"       
            
    for fname in os.listdir(_path):
        pathstr = "{}\{}".format(_path, fname)
        count_files = count_files + 1

        #print(pathstr)
        if os.path.isfile(pathstr):
            #print('exist {}'.format(fname))
            with open(pathstr, 'r') as f:
                s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
                strpos = s.find(bytes(strfind, 'utf-8'))
                if strpos != -1:
                    print(' ')
                    print('  ---------------------------------------------------')
                    print('  exists in file {} in line {}'.format(pathstr,strpos))
                    print('  ---------------------------------------------------')
                    
                    lines_file = list(filter(lambda line: line.find(strfind) >= 0, f.readlines()))
                    count_files_find = count_files_find + 1

                    for line in lines_file:
                        print('  *** {}'.format(line))
                    
    print('''
--------------------------------------------------------------   
PROCESO FINALIZADO - RESUMEN
--------------------------------------------------------------   
  PATH     :  {}
  STRING   :  {}
--------------------------------------------------------------   
  Archivos revisados      :   {}
  Archivos encontrados    :   {}
--------------------------------------------------------------   
    '''.format(_path, strfind, count_files, count_files_find))

    
def run():

    _exec_process = 0
    _leer_argumentos()
    
    _path = sys.argv[1]
    _prm_str = sys.argv[2]

    print('''
--------------------------------------------------------------   
BUSQUEDA DE DATOS
PATH     :  {}
STRING   :  {}
--------------------------------------------------------------   
    '''.format(_path, _prm_str))

    if(len(_prm_str) > 0): 
        _buscar_datos(_prm_str, _path)

    print('-------------------------------------------------------------- '.format(_path, _prm_str))

if __name__ == '__main__':
    run()