# Reporte de Análisis de Datos - Pandas

`Pedro Martinez Machine Learning pandas, NC 0093`

## 1. DataFrame Convertido
```text
     Laboratorio  Equipos  Investigadores
0        Química       45              15
1       Biología       30              12
2         Física       25              10
3    Computación       60              20
4  Investigación       40              18
5       Análisis       35              14
```

## 2.1 Primeras Filas (head)
```text
  Laboratorio  Equipos  Investigadores
0     Química       45              15
1    Biología       30              12
```

## 2.2 Últimas Filas (tail)
```text
     Laboratorio  Equipos  Investigadores
4  Investigación       40              18
5       Análisis       35              14
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Laboratorio         str
Equipos           int64
Investigadores    int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column          Non-Null Count  Dtype
---  ------          --------------  -----
 0   Laboratorio     6 non-null      str  
 1   Equipos         6 non-null      int64
 2   Investigadores  6 non-null      int64
dtypes: int64(2), str(1)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de la Columna 'Equipos'
```text
count     6.000000
mean     39.166667
std      12.416387
min      25.000000
25%      31.250000
50%      37.500000
75%      43.750000
max      60.000000
Name: Equipos, dtype: float64
```

## 4. Ordenar Ascendente por Equipos
```text
     Laboratorio  Equipos  Investigadores
2         Física       25              10
1       Biología       30              12
5       Análisis       35              14
4  Investigación       40              18
0        Química       45              15
3    Computación       60              20
```

## 5. Ordenar Descendente por Investigadores
```text
     Laboratorio  Equipos  Investigadores
3    Computación       60              20
4  Investigación       40              18
0        Química       45              15
5       Análisis       35              14
1       Biología       30              12
2         Física       25              10
```

`Pedro Martinez Machine Learning pandas, NC 0093`