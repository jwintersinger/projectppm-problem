Python information
------------------
Python version: `Python 3.7.5 (default, Oct 25 2019, 15:51:11)`
(This is the Linux `x86_64` version of Anaconda.)

Prereqs for running examples:
  
    * Example 1: needs Python 3 and NumPy
    * Example 2: doesn't need anything

Compiling
------------------
    # I have tried with GCC 7.3.0 and 9.2.0 on two different systems.
    cd projectppm
    bash make.sh

Example 1
---------
The NaN bug can be reproduced by running `python3 example1.py`. This loads the
`adj`, `phi_hat`, and `var_phi_hat` arrays from the `example1.npz` file and
calls your projection code using `ctypes`. All 31 values in the returned `M`
array are NaN, despite none of the inputs passed to `tree_cost_projection()`
being NaN.

The really weird part is that the bug is stochastic. Using the *exact same*
inputs, the first 18 calls will succeed. The 19th call, however, returns all
NaNs.

Example 2
---------
The NaN bug can be reprouced by running `bash example2.sh`. This pipes
`example2.txt` to the `projectppm` binary, which writes its result on stdout.
Here the bug isn't stochastic -- every attempt seems to reliably return all
NaNs.
