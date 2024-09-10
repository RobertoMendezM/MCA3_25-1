%{
             PROGRAMA UsaRocketTrajectory.m 
 USANDO  ode45  y ode15s,  SE RESUELVE EL SISTEMA DE 
 ECUACIONES DIFERENCIALES ORDINARIAS  DEL MODELO DE TRAYECTORIA
 DE UN COHETE QUE ESTA DEFINIDO EN
                    RocketTrajectory.m
  Y  SE GRAFICAN ALGUNOS RESULTADOS.

  Las funciones ode regresan un vector de la forma
  [T, Y], siendo:          
  T : vector columna de tiempos
  Y : matriz de dimensión length(T)x3 donde cada columna 
     representa las siguientes variables 
                [m , h , V] 
   m masa
   h altura
   V velocidad
      
 Autor:  ROBERTO MÉNDEZ MÉNDEZ
                   
 Última revisión: 8 Sep 24
%}
close all
clear
clc
% Intervalo de tiempo
t = [0 7];

% Valores iniciales
m_seca = 2.2;
m_fuel = 0.625;
m_f0 = 5/16;
ue = 960;
g = 9.78;
m0 = m_seca + m_fuel;
h0 = 0;
V0 = (m_f0*ue - m0*g)/m0;
x = [m0 h0 V0];

%%  Solución con ode45

% Función para imponer la condición de paro en el método "ode" si la
% velocidad se vuelve negativa.
% En este caso Y(3) -> Valor velocidad
function [value, isterminal, direction] = stopCondition(T, Y)
    value      = (Y(3) < 0);  % Condición de Paro
    isterminal = 1;   % Detiene la integración
    direction  = 0;
end

options = odeset('Events',@stopCondition);
[T,Y,te,ye,ie] = ode45(@RocketTrajectory,t,x, options);



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                     GRÁFICAS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

figure('NumberTitle','off','Name', 'Velocidad vs Tiempo',...
       'Position', [60 , 220, 550,420])
plot(T(:),Y(:,3))
xlrk = {'tiempo (ms)'};    
xlabel(xlrk)
ylabel('Velocidad [m/s]')
title('Velocidad vs Tiempo')

figure('NumberTitle','off','Name', 'Altura vs Tiempo',...
       'Position', [250 , 220, 550,420])
plot(T(:),Y(:,2))
xlrk = {'tiempo (ms)'};    
xlabel(xlrk)
ylabel('Altura [m]')
title('Altura vs Tiempo')

figure('NumberTitle','off','Name', 'Masa vs Tiempo',...
       'Position', [440 , 220, 550,420])
plot(T(:),Y(:,1))
xlrk = {'tiempo (ms)'};    
xlabel(xlrk)
ylabel('Masa [Kg]')
title('Masa vs Tiempo')