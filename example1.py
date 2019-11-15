import numpy as np
import phi_fitter_projection as pf

def main():
  for trial in range(1000000):
    if trial % 100 == 0:
      print('iteration=%s' % trial)
    F = np.load('example1.npz')
    F = dict(F)

    eta = pf._fit_eta_S_ctypes(F['adj'], F['phi_hat'], F['var_phi_hat'])
    if np.any(np.isnan(eta)):
      print('Got', np.sum(np.isnan(eta)), 'NaNs on iteration', trial)
      break

main()
