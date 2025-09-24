#Versão oficial da análise

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import country_converter as coco

cc = coco.CountryConverter()

df = pd.read_csv('Agrofood_co2_emission.csv/Agrofood_co2_emission.csv')

df = df.dropna()
df = df.drop(columns=[
    "Pesticides Manufacturing",
    "Savanna fires",
    "Forest fires",
    "Net Forest conversion",
    "Fires in humid tropical forests",
    "Food Household Consumption",
    "Fires in organic soils",
    "Manure left on Pasture",
    "Manure applied to Soils",
    "Fertilizers Manufacturing"
])

df = df[df["Year"] >= 2010]

df["Continent"] = cc.convert(names=df["Area"], to="continent")

df["Total_Population"] = df["Total Population - Female"] + df["Total Population - Male"]

sns.set_theme(style="whitegrid")



#Relação entre IPPU e emissões totais
def ippu_emissoes(int=0):
    if int != 0:
        print("""A análise entre a relação entre IPPU (Industrial Processes and Product Use) e as emissões totais de CO2 pode revelar insights importantes sobre como as atividades industriais impactam o meio ambiente. O IPPU inclui emissões provenientes de processos industriais, como a produção de cimento, aço, produtos químicos e outros materiais. Essas atividades são frequentemente associadas a altos níveis de emissões de gases de efeito estufa.""")
    else:
        sns.scatterplot(
            data=df,
            x="IPPU",
            y="total_emission",
            hue="Continent",
            sizes=(50, 300),
            palette="tab10"
        )
        plt.title("Relação entre IPPU e Emissões Totais por Continente")
        plt.xlabel("IPPU")
        plt.ylabel("Total de Emissões")
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
        plt.show()

# Barras - evolução emissões
def barras_evolucao_emissoes(int=0):
    if int != 0:
        print("""A análise da evolução das emissões de CO2 ao longo dos anos pode fornecer insights valiosos sobre as tendências e padrões de emissão. Essa análise pode ajudar a identificar períodos de aumento ou diminuição das emissões, bem como a avaliar o impacto de políticas e práticas sustentáveis ao longo do tempo.""")
    else:
        sns.barplot(data=df, x="Year", y="total_emission", hue="Continent", ci=None)
        plt.title("Evolução das Emissões por Continente")
        plt.xlabel("Year")
        plt.ylabel("total_emission")
        plt.show()
# Linha - temperatura média
# Linha - temperatura média
def linha_temperatura_media(int=0):
    if int != 0:
        print("""A análise da evolução da temperatura média ao longo dos anos pode fornecer insights valiosos sobre as tendências climáticas e os impactos das mudanças climáticas influenciadas pelas emissões de CO2. Essa análise pode ajudar a identificar padrões de aquecimento ou resfriamento, bem como a avaliar o impacto das atividades humanas no clima global. Essa análise tem como objeto mostrar SOMENTE a evolução da temperatura média, sem considerar outras variáveis.""")
    else:
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=df, x="Year", y="Average Temperature °C", hue="Continent", marker="o", ci=None)
        plt.title("Evolução da Temperatura Média por Continente")
        plt.xlabel("Year")
        plt.ylabel("Average Temperature °C")
        plt.show()

# Dispersão emissões x temperatura
def dispersao_emissoes_temperatura(int=0):
    if int != 0:
        print("""A análise da relação entre as emissões de CO2 e a temperatura média pode fornecer insights importantes sobre como as atividades humanas, especialmente aquelas relacionadas à agropecuária, impactam o clima global. Emissões elevadas de CO2 estão associadas ao efeito estufa, que contribui para o aquecimento global e mudanças climáticas. Ao examinar essa relação, podemos entender melhor como diferentes continentes estão sendo afetados por essas emissões e como isso se reflete nas variações de temperatura média. Essa análise é mais precisa que a de linha, pois mostra a dispersão dos dados e possíveis correlações entre as variáveis.""")
    else:
        sns.scatterplot(
            data=df,
            x="total_emission",
            y="Average Temperature °C",
            hue="Continent"
        )
        plt.title("Relação entre Emissões e Temperatura Média por Continente")
        plt.show()

# Dispersão emissões x transporte
def dispersao_emissoes_transporte(int=0):
    if int != 0:
        print("""A análise da relação entre as emissões de CO2 e o transporte de alimentos pode fornecer insights importantes sobre como a logística e a cadeia de suprimentos impactam o meio ambiente. O transporte de alimentos, especialmente quando envolve longas distâncias e modos de transporte intensivos em carbono, pode contribuir significativamente para as emissões totais de CO2 associadas à agropecuária. Ao examinar essa relação, podemos identificar padrões e tendências que podem ajudar a informar políticas e práticas mais sustentáveis na cadeia de suprimentos alimentares. Essa análise é relevante para entender como diferentes continentes estão lidando com o transporte de alimentos e suas implicações ambientais.""")
    else:
        sns.scatterplot(
            data=df,
            x="total_emission",
            y="Food Transport",
            hue="Continent"
        )
        plt.title("Relação entre Transporte de Comida e Emissões por Continente")
        plt.show()

# Boxplot energia nas fazendas
def boxplot_energia_fazendas(int=0):
    if int != 0:
        print("""A análise do uso de energia em fazendas por continente pode fornecer insights valiosos sobre as práticas agrícolas e a eficiência energética em diferentes regiões do mundo. O uso de energia em fazendas inclui a energia consumida para operações agrícolas, como irrigação, maquinário, processamento de alimentos e outras atividades relacionadas à produção agrícola. Ao examinar essa variável por continente, podemos identificar padrões e diferenças nas práticas agrícolas, bem como avaliar o impacto ambiental associado ao uso de energia na agricultura.""")
    else:
        sns.boxplot(
            data=df,
            x="Continent",
        y="On-farm energy use"
      )
        plt.yscale("log")
        plt.title("Distribuição do uso de energia em fazendas por Continente")
        plt.ylabel("On-farm energy use")
        plt.xlabel("Continent")
        plt.show()

# População x emissões
def dispersao_populacao_emissoes(int=0):
    if int != 0:
        print("""A análise da relação entre a população total e as emissões de CO2 pode fornecer insights importantes sobre como o crescimento populacional e as atividades humanas impactam o meio ambiente. Em geral, um aumento na população pode levar a um aumento nas emissões de CO2 devido à maior demanda por recursos, energia e transporte. No entanto, essa relação pode variar significativamente entre diferentes continentes devido a fatores como níveis de desenvolvimento econômico, políticas ambientais e práticas sustentáveis. Ao examinar essa relação, podemos identificar padrões e tendências que podem ajudar a informar políticas e estratégias para mitigar as emissões de CO2 em diferentes regiões do mundo.""")
    else:
        sns.scatterplot(data=df, y="Total_Population", x="total_emission", hue="Continent")
        plt.title("Relação entre população e emissões de carbono por continente")
        plt.ylabel("Total_Population")
        plt.xlabel("total_emission")
        plt.show()


menu = """
Para as análises a seguir, foi usado um dataset sobre as emissões de CO2 relacionadas à agropecuária, que inclui dados sobre diferentes continentes, anos, tipos de emissões e outros fatores relevantes.
As análises geradas a partir do dataset estão abaixo. Escolha o tipo de visualização que deseja:
1- Relação entre IPPU e emissões totais
2- Barras - evolução emissões
3- Linha - temperatura média
4- Dispersão emissões x temperatura
5- Dispersão emissões x transporte
6- Boxplot energia nas fazendas
7- População x emissões
8- Dúvida sobre análise
0- Sair
"""
while True:
    print(menu)
    escolha = input("Digite o número da análise que deseja visualizar (ou 0 para sair): ")

    match escolha:
        case '1':
            ippu_emissoes()
        case '2':
            barras_evolucao_emissoes()
        case '3':
            linha_temperatura_media()
        case '4':
            dispersao_emissoes_temperatura()
        case '5':
            dispersao_emissoes_transporte()
        case '6':
            boxplot_energia_fazendas()
        case '7':
            dispersao_populacao_emissoes()
        case '8':
            menu2 = """
        Escolha a análise sobre a qual você tem dúvida:
        1- Relação entre IPPU e emissões totais
        2- Barras - evolução emissões
        3- Linha - temperatura média
        4- Dispersão emissões x temperatura
        5- Dispersão emissões x transporte
        6- Boxplot energia nas fazendas
        7- População x emissões
        8- Por que a análise é sobre agropecuária?
        9- Voltar ao menu principal
        0- Sair
            """
            while True:
                print(menu2)
                escolha2 = input("Digite o número da análise sobre a qual você tem dúvida (ou 0 para sair): ")
                match escolha2:
                    case '1':
                        ippu_emissoes(int=1)
                    case '2':
                        barras_evolucao_emissoes(int=1)
                    case '3':
                        linha_temperatura_media(int=1)
                    case '4':
                        dispersao_emissoes_temperatura(int=1)
                    case '5':
                        dispersao_emissoes_transporte(int=1)
                    case '6':
                        boxplot_energia_fazendas(int=1)
                    case '7':
                        dispersao_populacao_emissoes(int=1)
                    case '8':
                        print("""A análise é focada na agropecuária porque esse setor é um dos maiores contribuintes para as emissões globais de CO2 e outros gases de efeito estufa. A produção agrícola, incluindo o cultivo de plantas e a criação de animais, envolve várias atividades que geram emissões significativas, como o uso de fertilizantes, manejo do solo, fermentação entérica em ruminantes e desmatamento para expansão agrícola. Além disso, a agropecuária está diretamente ligada à segurança alimentar e ao desenvolvimento econômico em muitas regiões do mundo. Portanto, entender as emissões associadas a esse setor é crucial para desenvolver estratégias eficazes de mitigação das mudanças climáticas e promover práticas agrícolas mais sustentáveis. Além disso, o projeto do aplicativo Calbon é focado nas emissões de CO2 das industrias em geral e os dados sobre outras indústrias são escassos ou incompletos, esse dataset foi um dos melhores encontrados pela equipe de Dados do Calbon.""")
                    case '9':
                        break
                    case '0':
                        print("Saindo")
                        exit()
                    case _:
                        print("Escolha inválida. Tente novamente.")
        case '0':
            print("Saindo")
            break
        case _:
            print("Escolha inválida. Tente novamente.")
