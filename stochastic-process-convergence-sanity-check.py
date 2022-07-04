# (i)python 3.6
# import this as module
import numpy as np
import matplotlib.pyplot as plt
# *normalized* matr and vec
def get_rand_vec(s): 
    _z = np.random.rand(s)
    _z /= np.sum(_z)
    return _z
def get_rand_matr(_m,_n):
    _A = np.zeros((_m,_n))
    for i in range(_n):
        _A[:,i]=get_rand_vec(_m)
    return _A
# Plot an NxN stoch process course over t time. decrease step_factor for 
#     smaller steps.  Originally for a self-check that linear stoch processes 
#     move exponentially (with small enough step_factor)
def plot_results(results):
    for j in range(results.shape[0]):
        plt.plot(results[j,:])
    plt.show()
def chart_process(N=10, t=None, step_factor=1.0, seed=None, autoscale=True,
        deltas=False, ret=False
        ):
    if t==None: t=15
    else: autoscale=False
    if not seed:
        seed=np.random.randint(1000)
        print("Seed: "+str(seed))
    np.random.seed(seed)
    M = get_rand_matr(N,N)
    x = x0 = get_rand_vec(N)
    if step_factor<1 and autoscale: t=int(t/step_factor)
    results = np.empty( ( x.shape[0], t) )
    for i in range(t):
        results[:,i] = x = ( M @ x )*step_factor + x*(1-step_factor)

    if deltas: results=(results[:,1:] - results[:,:-1])

    plot_results(results)

    if ret: return results

if __name__=='__main__': 
    chart_process( N=12, step_factor=0.05, t=50, seed=828)

