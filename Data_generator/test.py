import functions as f
import func_generator as fg
import matplotlib.pyplot as plt
import PARAMS as P
import numpy as np

func_list = np.array([f.linear, f.sin, f.exp, f.ln, f.sqrt, f.my_abs, f.sqr, f.hyper])

def test_one_gen():
    for f in func_list:
        res_f, res_f_name = fg.generate_single_function(f)
        print(res_f_name)
        x = np.arange(P.x_interval[0],P.x_interval[1],0.01)
        y = np.array([res_f(i) for i in x])
        plt.plot(x,y)
        plt.show()


def test_complex_func():
    f, s = fg.generate_complex_function(func_list,4)
    print(s)
    
    x = np.arange(P.x_interval[0],P.x_interval[1],0.01)
    y = np.array([f(i) for i in x])
    plt.plot(x,y)
    plt.show()
    

def test_data_generator():
    fun, s = fg.generate_complex_function(np.array([f.sin]),3, chances_count= 3)
    print(s)
    x,y = fg.generate_dataset(fun, noise_ratio=0.5)
    fx = np.arange(P.x_interval[0],P.x_interval[1],0.01)
    fy = np.array([fun(i) for i in fx])
    err = np.mean((y-[fun(i) for i in x])**2)
    print('Mean square error = ', err)
    plt.plot(fx,fy)
    plt.scatter(x,y)
    plt.show()    
    
#test_one_gen()    
#fg.generate_complex_function(np.array([f.linear]))
#test_complex_func()
test_data_generator()