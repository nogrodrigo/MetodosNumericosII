#include <limits>
#include <math.h>
#include <iostream>

# define M_PI  3.14159265358979323846

double f (double x)
{
  return 1.0 / powf(x*x, 1.0/3.0);
}

double x_s (double ini, double fim, double s)
{
  return ( ( ini + fim ) / 2.0 ) + ( ( ( fim - ini ) / 2.0 ) * tanh(s) );
}

double s_barra (double ini, double fim, double s)
{
  return ( ( fim + ini ) / 2.0 ) + ( ( ( fim - ini ) / 2.0 ) * s );
}

double f_barra(double ini, double fim, double s)
{
  return f(x_s(ini, fim, s))
       * ( ( fim - ini ) / 2.0 )
       * ( 1.0 / pow( cosh(s), 2 ) );
}

double GaussHermitExpSimples (double ini, double fim, int grau)
{
  double w1, w2, w3;
  double s1, s2, s3;
  double resultado;

  switch (grau)
  {
  case 2:
    s1 = - ( 1.0 / sqrt(2) );
    s2 = + ( 1.0 / sqrt(2) );
    w1 = w2 = sqrt(M_PI) / 2.0;

    resultado = ( exp(s1 * s1) * f_barra( ini, fim, s1 ) * w1 )
              + ( exp(s2 * s2) * f_barra( ini, fim, s2 ) * w2 );
    break;
  case 3:
    s1 = - sqrt( 3.0 / 2.0 );
    s2 = 0.0;
    s3 = + sqrt( 3.0 / 2.0 );
    w1 = w3 = sqrt(M_PI) / 6.0;
    w2 = ( 2.0 * sqrt(M_PI) ) / 3.0;

    resultado = ( exp(s1 * s1) * f_barra( ini, fim, s1 ) * w1 )
              + ( exp(s2 * s2) * f_barra( ini, fim, s2 ) * w2 )
              + ( exp(s3 * s3) * f_barra( ini, fim, s3 ) * w3 );
  break;
  }

  return resultado;
}

double GaussLegendreExpSimples (double ini, double fim, double iniC, double fimC, int qtdPontos)
{
  double resultado;
  double w1, w2, w3;
  double s1, s2, s3;

  switch (qtdPontos)
  {
  case 2:
    w1 = w2 = 1.0;
    s1 = - 1.0 / sqrt( 3.0 );
    s2 = + 1.0 / sqrt( 3.0 );

    resultado = ( ( fimC - iniC ) / 2.0 ) * ( ( f_barra( ini, fim, s_barra( iniC, fimC, s1 ) ) * w1 )
                                            + ( f_barra( ini, fim, s_barra( iniC, fimC, s2 ) ) * w2 ) );
    break;
  case 3:
    w1 = w3 = 5.0 / 9.0;
    w2 = 8.0 / 9.0;

    s1 = - sqrt( 3.0 / 5.0 );
    s2 = 0.0;
    s3 = + sqrt( 3.0 / 5.0 );

    resultado = ( ( fimC - iniC ) / 2.0 ) * ( ( f_barra( ini, fim, s_barra( iniC, fimC, s1 ) ) * w1 )
                                            + ( f_barra( ini, fim, s_barra( iniC, fimC, s2 ) ) * w2 )
                                            + ( f_barra( ini, fim, s_barra( iniC, fimC, s3 ) ) * w3 ) );
  }

  return resultado;
}

double GaussLegendreParticoesExpSImples (double ini, double fim, double iniC, double fimC, int qtdPontos, double eps)
{
  double integralNova = std::numeric_limits<double>::infinity();
  double integralVelha;
  int N = 1;

  do
  {
    integralVelha = integralNova;

    double deltaX = ( fimC - iniC ) / N;

    integralNova = 0.0;

    for ( int i = 0; i < N; i++ )
    {
      double xIn = iniC + ( i * deltaX );
      double xFin = xIn + deltaX;
      integralNova += GaussLegendreExpSimples( ini, fim, xIn, xFin, qtdPontos );
    }

    N *= 2;
  } while (fabs( ( integralNova - integralVelha ) / integralNova ) > eps );

  return integralNova;
}


int main()
{
  double a;
  double b;
  double cInicial;
  double c;
  double eps;
  double passo;
  int qtdPontos;
  int grau;

  std::cout << "Integração de Gauss Legendre" << std::endl;

  std::cout << "Início do intervalo: ";
  std::cin >> a;

  std::cout << "Fim do intervalo: ";
  std::cin >> b;

  //std::cout << "Número de grau de Hermit: ";
  //std::cin >> grau;

  std::cout << "Quantidade de pontos de Legendre: ";
  std::cin >> qtdPontos;

  std::cout << "Insira o valor do corte: ";
  std::cin >> cInicial;

  std::cout << "Tolerância: ";
  std::cin >> eps;

  double resultadoAnt;
  double resultadoNovo = std::numeric_limits<double>::infinity();

  //double resultado = GaussHermitExpSimples(a, b, grau);

  c = cInicial;
  passo = 0.1;

  do
  {
    resultadoAnt = resultadoNovo;

    resultadoNovo = GaussLegendreParticoesExpSImples(a, b, -c, c, qtdPontos, eps);

    c += passo;

    if (isnan( resultadoNovo ) || isinf( resultadoNovo ))
    {
      c = cInicial;
      passo /= 10;
      resultadoNovo = std::numeric_limits<double>::infinity();
      continue;
    }

  } while (fabs( ( resultadoNovo - resultadoAnt ) / resultadoNovo ) > eps);

  std::cout << resultadoNovo << " - " << c - passo << std::endl;

  return 0;
}