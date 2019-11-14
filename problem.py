import numpy as np
import phi_fitter_projection as pf

def main():
  F = np.load('problem.npz')
  F = dict(F)

  for trial in range(1000000):
    if trial % 100 == 0:
      print(trial)

    eta = pf._project_ppm(f['adj'], f['phi_hat'], f['var_phi_hat'], 0)
    #eta = pf._fit_eta_S_subprocess(f['adj'], f['phi_hat'], f['var_phi_hat'])
    #eta = pf._fit_eta_S_ctypes(f['adj'], f['phi_hat'], f['var_phi_hat'])

    if np.any(np.isnan(eta)):
      print('nan', trial, np.sum(np.isnan(eta)))
      break

main()
