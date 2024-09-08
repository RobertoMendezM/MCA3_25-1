%{
             PROGRAMA 
 IMPLEMENTACIÓN DEL MODELO PARA TRAYECTORIA DE UN COHETE 
 Concurso UNAM

Referencias:
    *Trajectory Calculation Lab 2 Lecture Notes pdf
     https://web.mit.edu/16.unified/www/FALL/systems/Lab_Notes/traj.pdf
    * Simulación 1 DoF -Propulsión UNAM pdf

Modelo a Programar:
  
  dm/dt = -m_f
  dh/dt = V
  dV/dt = -g - r*V*|V|*C_d*A/(2*m) + V*m_f*u_e/(|V|*m)

  NOTA!!! = Si A es grande la velocidad solo disminuye
            pues pesa mucho el segundo término
            Con A <= .05 la Velocidad ya tiene un lapso de crecimiento
 

FUNCIÓN PROGRAMADA 
 La función  RocketTrajectory(t,x) consta de dos parámetros t,x
                (t,x)
 donde
   t es el intervalo de tiempo 
   x = [m0 h0 V0] es el  vector de valores iniciales
  
  Interpretación de los x(i)
   x(1)  valores de m 
   x(2)  valores de la latura h
   x(3)  valores de la velocidad V


 Autor: ROBERTO MÉNDEZ MÉNDEZ
 
 Última revisión: 8 Sep 2024
%}

function dxdt = RocketTrajectory(t,x)

    g = 9.78;
    r = 1;
    C_d = 0.75; 
    A = .05; 
    u_e = 960;
    if 0 <= t && t <= 2
        m_f = 5/16;
    else
        m_f = 0;
    end
   
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  %   Ecuaciones diferenciales
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    dxdt = [-m_f; ...
             x(3); ...
            -g - r*x(3)*abs(x(3))*C_d*A/(2*(x(1))) + ...
                   x(3)*m_f*u_e/(abs(x(3))*x(1))];
   