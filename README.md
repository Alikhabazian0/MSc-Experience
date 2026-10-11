# Physics Coursework and Projects

**Numerical simulations, course projects, and scientific reports from my BSc and MSc studies in physics.**

This repository brings together my work in computational physics, statistical physics, quantum mechanics, critical phenomena, complex systems, stochastic processes, and optimization. It includes Python scripts, Jupyter notebooks, selected results, and project reports that connect theoretical models with numerical calculations and visualization.

My BSc studies were completed at **Iran University of Science and Technology**, and my MSc studies in **Statistical Physics and Complex Systems** at **Shahid Beheshti University**. The collection documents coursework and exploratory implementations developed during these degrees.

[Coursework](#coursework) · [Featured projects](#featured-projects) · [Selected outputs](#selected-outputs) · [Getting started](#getting-started)

## Coursework

| Course or subject | Topics and examples | Materials |
| --- | --- | --- |
| [Numerical Simulation — BSc](./Numerical%20Simulation%20-%20Bsc/) | Numerical integration, Runge–Kutta methods, random walks, spin configurations, molecular dynamics, and numerical solutions of the Schrödinger equation | Python scripts and selected outputs |
| [Advanced Computational Physics](./Advanced%20Computational%20Phyiscs/) | Harmonic-oscillator integration, interpolation, Fourier methods, Monte Carlo integration, probability distributions, surface growth, and fractal box counting | Python scripts, figures, and a sample dataset |
| [Advanced Quantum Mechanics](./Advanced%20Quantum%20Mechanics/) | A symmetric double-well model with a central barrier; numerical energy calculations, wave functions, and superposition visualizations | Project notebook and figures |
| [Critical Phenomena](./Critical%20Phenomena/) | Renormalization-group flow calculations, coupling-space vector fields, and comparisons across spatial dimensions | Jupyter notebooks, a Wolfram notebook, and figures |
| [Physics of Complex Systems](./Physics%20of%20Complex%20Systems/) | Surface-growth simulations, structure functions, and structural-balance dynamics in signed networks | Notebooks, scripts, figures, reports, and a presentation |
| [Stochastic Processes](./Stochastic%20Processes/) | Brownian motion, autocorrelation, Pearson correlation, mutual information, and sample-size effects | Python scripts and Jupyter notebooks |
| [Optimization Methods in Physics](./Optimization%20Methods%20in%20Physics/) | Optimization exercises, nonlinear dynamics, random walks, Langevin simulations, Monte Carlo sampling, and financial modelling | Exercise notebooks, scripts, figures, and a project with reports |

## Featured projects

### Computational physics methods for portfolio risk and option pricing

**Course:** Optimization Methods in Physics  
**Supervisor:** Prof. S. M. S. Movahed

This project applies stochastic simulation and numerical methods to financial modelling. It begins with Monte Carlo portfolio simulation, using Cholesky decomposition to generate asset returns with a specified covariance structure. The resulting portfolio-value distribution is used to estimate **value at risk (VaR)** and **conditional value at risk (CVaR)**.

The option-pricing component simulates risk-neutral geometric Brownian motion and estimates European option values from discounted payoffs. It investigates **antithetic variates**, **delta-based control variates**, and combinations involving **gamma controls**, comparing estimator uncertainty and computational cost. A separate stochastic-calculus notebook develops random walks, Brownian motion, and geometric Brownian motion. The final notebook compares loop-based and vectorized implementations of **binomial option pricing**.

Together, these examples connect methods from computational and statistical physics with portfolio risk and derivative valuation. The report explains the model assumptions and distinguishes theoretical variance-reduction principles from the results of the individual numerical examples.

**Explore the project:**

- [English report](./Optimization%20Methods%20in%20Physics/Project/Reports/English_Report.pdf)
- [Persian report](./Optimization%20Methods%20in%20Physics/Project/Reports/Persian_Report.pdf)
- [Monte Carlo methods in finance](./Optimization%20Methods%20in%20Physics/Project/1.1%20Monte%20Carlo%20Methodes%20in%20Finance.ipynb)
- [Stochastic calculus in finance](./Optimization%20Methods%20in%20Physics/Project/1.2%20Stochastic%20Calculus%20in%20Finance.ipynb)
- [Binomial option pricing](./Optimization%20Methods%20in%20Physics/Project/1.3%20Binomial%20Option%20Pricing%20in%20Finance.ipynb)

### Structural balance dynamics at nonzero temperature

**Course:** Physics of Complex Systems  
**Supervisor:** Prof. Reza Jafari

This project studies **structural balance in signed networks**, where positive and negative edges represent friendly and hostile relationships. A triad is balanced when the product of its three edge signs is positive. The finite-temperature model assigns an energy to each triad and introduces stochasticity through a temperature parameter, allowing the network to explore both balanced and frustrated configurations.

The work examines a **triadic Hamiltonian**, **mean-field self-consistency equations**, and **Metropolis Monte Carlo dynamics**. Numerical examples investigate the dependence of self-consistent solutions and mean triad energy on temperature, alongside the effects of initial configurations. The report compares selected calculations with published results and discusses the stability of branches and the role of competing states. It also considers a related **quartic-balance model** to examine how higher-order interactions alter the possible stable configurations.

The project connects statistical mechanics with collective organization in social networks. Its report distinguishes qualitative reproduction of the published branch structure from conclusions that require longer simulations or more detailed numerical validation.

**Explore the project:**

- [English report](./Physics%20of%20Complex%20Systems/Project/Reports/English_Report.pdf)
- [Presentation](./Physics%20of%20Complex%20Systems/Project/Reports/Presentation.pdf)
- [Persian report](./Physics%20of%20Complex%20Systems/Project/Reports/Persian_Report.pdf)
- [Project notebook](./Physics%20of%20Complex%20Systems/Project/Project_codes.ipynb)
- [Project folder and simulation outputs](./Physics%20of%20Complex%20Systems/Project/)

## Selected outputs

The following figures are examples of outputs included in the coursework. Each image links to its original file; the associated notebook provides the equations and simulation settings.

### Renormalization-group flow for d = 5

Coupling-space flow in the Critical Phenomena exercises for $d=5$, with $\epsilon=4-d=-1$. Streamlines show the direction of the implemented vector field, and color indicates its magnitude.

[![Renormalization-group flow in the u-v plane for d equal to 5](./Critical%20Phenomena/Results/Rg%20flow%20for%20d%3D5.png)](./Critical%20Phenomena/Results/Rg%20flow%20for%20d%3D5.png)

[View the RG-flow notebook](./Critical%20Phenomena/RG%20Flow%20Pattern%20-%20Ex7.ipynb)

### Phase-space projections of the Lorenz system

The $x$–$y$, $x$–$z$, and $y$–$z$ projections of a numerical Lorenz-system trajectory from Set 5 of Optimization Methods in Physics. The example uses $\sigma=10$, $\rho=28$, and $\beta=8/3$.

[![Three phase-space projections of the Lorenz system](./Optimization%20Methods%20in%20Physics/Exercises/Set5/Phase%20Diagrams.png)](./Optimization%20Methods%20in%20Physics/Exercises/Set5/Phase%20Diagrams.png)

[View the nonlinear-dynamics notebook](./Optimization%20Methods%20in%20Physics/Exercises/Set5/Set5.ipynb)

### Velocity probability density from a Langevin simulation

Estimated joint probability density of $v(t)$ and $v(t+\tau)$ for a simulated Langevin particle, from Set 6 of Optimization Methods in Physics. The concentration along the diagonal illustrates the dependence between velocities separated by the selected time lag.

[![Joint probability density of a Langevin particle's velocity at two times](./Optimization%20Methods%20in%20Physics/Exercises/Set6/Probability%20Density%20plot.png)](./Optimization%20Methods%20in%20Physics/Exercises/Set6/Probability%20Density%20plot.png)

[View the random-walk and Langevin notebook](./Optimization%20Methods%20in%20Physics/Exercises/Set6/set6.ipynb)

### Lyapunov exponent of the logistic map

Finite-iteration estimates of the Lyapunov exponent as the logistic-map parameter $\mu$ varies. The calculation examines local expansion and contraction along simulated trajectories; positive Lyapunov exponents are associated with sensitivity to initial conditions.

[![Numerical Lyapunov-exponent estimates for the logistic map](./Optimization%20Methods%20in%20Physics/Exercises/Set5/Lyapunov%20Exponent%20for%20Logistic%20Map.png)](./Optimization%20Methods%20in%20Physics/Exercises/Set5/Lyapunov%20Exponent%20for%20Logistic%20Map.png)

[View the Lyapunov-exponent calculation](./Optimization%20Methods%20in%20Physics/Exercises/Set5/Set5.ipynb)

## Getting started

Clone the repository and enter its root directory:

```bash
git clone https://github.com/Alikhabazian0/Physics-Coursework-and-Projects.git
cd Physics-Coursework-and-Projects
```

Most examples use **Python**, **NumPy**, **SciPy**, and **Matplotlib**. Some notebooks also use pandas. For a basic notebook environment, install:

```bash
python -m pip install numpy scipy matplotlib pandas jupyter
python -m jupyter notebook
```

Open the notebook for the subject you want to explore. Individual examples may require additional packages:

| Package | Examples using it |
| --- | --- |
| `yfinance`, `pandas-datareader` | Financial data retrieval in the Monte Carlo project |
| `py-vollib` | Black–Scholes pricing and option sensitivities |
| `numba` | Selected surface-growth simulations |
| `emcee` | Markov chain Monte Carlo exercises |
| `opencv-python` | Image-based box-counting calculations |

The Wolfram `.nb` file and R script use their respective software environments. PDF reports and existing figures can be viewed without running the code.

### Working with the examples

Some files retain the paths, input data, and parameter settings used during the original coursework. Update local file paths and install the packages imported by the example before running it. For notebooks, review the cells and execute them in order; some exercise sets redefine functions between questions.

Random simulations can produce different results between runs. When making comparisons, check the random seed, number of samples, simulation horizon, and model parameters. The saved figures document selected runs and should be interpreted alongside the corresponding calculations and reports.

## Academic context

This repository is a record of my coursework and project development. The implementations include exercises, exploratory calculations, and comparisons with theoretical models. The accompanying reports provide the background, references, and discussion for the two featured projects.

## Author

**Ali Khabazian**  
Physics · Statistical Physics and Complex Systems · Computational Modelling

[GitHub profile](https://github.com/Alikhabazian0)
