# cu-rl-shivendra
Repo that contains solution of assignments posted in the `content` repo

[`vi_and_pi.py`](vi_and_pi.py) contains the solution to **assignment 1** which has the `policy evaluation, policy improvement, policicy iteration` and `value iteration` implemented for the `Frozen Lake` Gym environment.

### Results on Deterministic Frozen Lake

```ruby
-------------------------
Beginning Policy Iteration
-------------------------
Policy evaluation converged in 1 iterations
Policy improved. New policy =  [3 3 3 3 3 3 3 3 3 3 3 3 3 3 2 3]
Policy evaluation converged in 2 iterations
Policy improved. New policy =  [3 3 3 3 3 3 3 3 3 3 1 3 3 2 2 3]
Policy evaluation converged in 3 iterations
Policy improved. New policy =  [3 3 3 3 3 3 1 3 3 2 1 3 3 2 2 3]
Policy evaluation converged in 4 iterations
Policy improved. New policy =  [3 3 1 3 3 3 1 3 2 2 1 3 3 2 2 3]
Policy evaluation converged in 5 iterations
Policy improved. New policy =  [3 2 1 0 1 3 1 3 2 2 1 3 3 2 2 3]
Policy evaluation converged in 6 iterations
Policy improved. New policy =  [2 2 1 0 1 3 1 3 2 2 1 3 3 2 2 3]
Policy evaluation converged in 7 iterations
Policy improved. New policy =  [2 2 1 0 1 3 1 3 2 2 1 3 3 2 2 3]
Policy evaluation converged in 7 iterations
Policy improved. New policy =  [2 2 1 0 1 3 1 3 2 2 1 3 3 2 2 3]
===> Policy Iteration converged in 8 iterations
SFFF
FHFH
FFFH
HFFG
  (Right)
SFFF
FHFH
FFFH
HFFG
  (Right)
SFFF
FHFH
FFFH
HFFG
  (Down)
SFFF
FHFH
FFFH
HFFG
  (Down)
SFFF
FHFH
FFFH
HFFG
  (Down)
SFFF
FHFH
FFFH
HFFG
  (Right)
SFFF
FHFH
FFFH
HFFG
Episode reward: 1.000000
Policy : 
➜➜↓←
↓↑↓↑
➜➜↓↑
↑➜➜↑
-------------------------
Beginning Value Iteration
-------------------------
Value Iteration converged in 7 iterations
SFFF
FHFH
FFFH
HFFG
  (Right)
SFFF
FHFH
FFFH
HFFG
  (Right)
SFFF
FHFH
FFFH
HFFG
  (Down)
SFFF
FHFH
FFFH
HFFG
  (Down)
SFFF
FHFH
FFFH
HFFG
  (Down)
SFFF
FHFH
FFFH
HFFG
  (Right)
SFFF
FHFH
FFFH
HFFG
Episode reward: 1.000000
Policy : 
➜➜↓←
↓↑↓↑
➜➜↓↑
↑➜➜↑
```
