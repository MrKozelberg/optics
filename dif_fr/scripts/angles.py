import numpy as np
import matplotlib.pyplot as plt

def angles():
    m1 = np.arange(-3,4)
    theta1 = np.arcsin(m1 * 650e-9 / 0.52e-3) / np.pi * 180 * 60
    
    m2 = np.arange(-6,7)
    theta2 = np.arcsin(m2 * 650e-9 / 1.5e-3 / 2) / np.pi * 180 * 60
    
    return theta1, theta2

def i_plot(N, lambd, b, d, theta):
    k = 2 * np.pi / lambd
    I = (np.sin(k*b*np.sin(theta)/2) / (k*b*np.sin(theta)/2) * np.sin(k*d*N*np.sin(theta)/2) / np.sin(k*d*np.sin(theta)/2))**2
    
    fig = plt.figure(figsize=(9,6))
    ax = fig.add_subplot(1,1,1)
    
    ax.plot(theta/np.pi*180*60, I, color='black')   
    
    ax.set_xlim([min(theta/np.pi*180*60),max(theta/np.pi*180*60)])
    ax.set_yscale('log')
    ax.set_ylim([1e-3,5e2])
    
    ax.set_ylabel(r'Относительная интенсивность света $I/I_0$')
    ax.set_xlabel(r'Угол дифракции $\theta$, минуты')
    ax.set_title('N={}, λ = {:.2E} м, b={:.1E} м, d={:.1E} м'.format(N,lambd, b, d))
    
    # theta_imp = np.array([272+59/60+12/3600,272+54/60+0,272+50/60+37/3600,272+41/60+0,272+37/60+18/3600,272+33/60+1/3600])   
    # theta_theor = np.arcsin(6.5e-7/5.2e-4*np.array([3,2,1,-1,-2,-3])) / np.pi * 180 * 60
    
    # theta_theor = np.arcsin(650e-9/1.5e-3/2*np.array([6,5,4,3,2,1,-1,-2,-3,-4,-5,-6])) / np.pi * 180 * 60
    # theta_imp = np.array([272+53/60+13/3600,272+51/60+54/3600,272+51/60+13/3600,272+50/60+30/3600,272+48/60+47/3600,272+47/60+10/3600,
                          # 272+45/60+37/3600,272+44/60+6/3600,272+42/60+41/3600,272+41/60+41/3600,272+40/60+41/3600,272+39/60+23/3600])
    
    theta_theor = np.arcsin(np.array([1/2,0,-1/2])*lambd/b)
    theta_imp = np.array([272+47/60+21/3600,272+46/60+21/3600,272+45/60+22/3600])
    
    theta_imp *= 60
    theta_imp -= np.mean(theta_imp)
    
    for th in theta_imp:
        ax.vlines(th, 1e-5, 1e3, linestyle=':', color='black')
        
    fig.savefig('../plots/dif_{}.pdf'.format(N))
   
    return theta_imp, theta_theor
    
    
if __name__ == "__main__":
    theta = np.linspace(-0.5*10e-4, 0.5*10e-4, 10000)
    a1, a2 = i_plot(15,650e-9,1e-3,2e-3,theta)
    
    