import numpy as np
import pandas as pd

def expected_result(home,aw):
  dr=home-aw
  we=(1/(10**(-dr/400)+1))
  return [np.round(we,3),1-np.round(we,3)]

def actual_result(home,aw):
  if home<aw:
      wa=1
      wh=0
  else:
      wa=0
      wh=1
  return [wh,wa]

def calculate_elo(elo_h,elo_aw,home_score,away_score):
  wh,wa=actual_result(home_score,away_score)
  weh,weaw=expected_result(elo_h,elo_aw)
  if (wh == 1):
      k = 20 * ((abs(home_score - away_score) + 3)**0.8)/(7.5+(0.006*(wh-wa)))
  else:
      k = 20 * ((abs(home_score - away_score) + 3)**0.8)/(7.5+(0.006* (wa-wh)))
    
  
  elo_hn=elo_h+k*(wh-weh)
  elo_awn=elo_aw+k*(wa-weaw)
   
  return elo_hn,elo_awn

def soft_reset(final_elo):
    return (final_elo * 0.75) + (0.25 * 1505)

