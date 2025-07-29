from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .models import autenticar_usuario
from sklearn.ensemble import BaggingClassifier
import pandas as pd
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.ensemble import AdaBoostClassifier  
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

modelos_base = {
    "Árvore de Decisão": DecisionTreeClassifier(),
    "KNN": KNeighborsClassifier(),
    "Naive Bayes": GaussianNB(),
    "MLP": MLPClassifier(max_iter=1000)
}




def avaliacao_rf(X, y, criterion='gini', n_estimators=100):
    rf = RandomForestClassifier(
        criterion=criterion,
        n_estimators=n_estimators,
        random_state=2
    )
    
    # 10-Fold Cross-Validation
    cv_scores = cross_val_score(rf, X, y, cv=10, scoring='accuracy')
    cv_mean = cv_scores.mean()
    
    # Divisões treino-teste
    split_results = {}
    for test_size in [0.1, 0.2, 0.3]:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=2)
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_test)
        
        acc = accuracy_score(y_test, y_pred)
      
        split_name = f"{int((1-test_size)*100)}/{int(test_size*100)}"
        split_results[split_name] = {
            "Acurácia": acc,
        }
    
    return {"10-Fold CV": cv_mean, **split_results}

X = 1
y = 2





test_sizes = [0.1, 0.2, 0.3]  # 90/10, 80/20, 70/30

# Tabela 1: Configuração Padrão (sem feature selection)

test_sizes = [0.1, 0.2, 0.3]  # 90/10, 80/20, 70/30
criteria = ['gini', 'entropy', 'log_loss']  # Critérios de divisão
n_estimators_list = [10, 100]  # Número de árvores
# Avaliando todas as combinações de parâmetros

results_rf = {}

# Resultados para GINI
results_rf["gini-10"] =  avaliacao_rf(X, y, criterion='gini', n_estimators=10)
results_rf["gini-100"] =  avaliacao_rf(X, y, criterion='gini', n_estimators=100)

# Resultados para Entropy
results_rf["entropy-10"] =  avaliacao_rf(X, y, criterion='entropy', n_estimators=10)
results_rf["entropy-100"] =  avaliacao_rf(X, y, criterion='entropy', n_estimators=100)

# Resultados para log_loss
results_rf["loss-10"] =  avaliacao_rf(X, y, criterion='log_loss', n_estimators=10)
results_rf["loss-100"] =  avaliacao_rf(X, y, criterion='log_loss', n_estimators=100)
       

from sklearn.ensemble import StackingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score




def avaliar_stacking(X, y, test_size=0.3):
    # Modelos base diretamente definidos
    knn = KNeighborsClassifier()
    mlp = MLPClassifier(max_iter=300, random_state=3)
    
    # Modelo final (meta-aprendizado)
    final_estimator = LogisticRegression(max_iter=300, random_state=4)
    
    # Stacking com dois classificadores base
    stacking = StackingClassifier(
        estimators=[('knn', knn), ('mlp', mlp)],
        final_estimator=final_estimator,
        cv=3,
        n_jobs=-1,
        verbose=1
    )
    
    # Avaliação com 10-Fold Cross-Validation
    cv_scores = cross_val_score(stacking, X, y, cv=10, scoring='accuracy', error_score='raise')
    cv_mean = cv_scores.mean()
    
    # Avaliação com divisão treino/teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    stacking.fit(X_train, y_train)
    y_pred = stacking.predict(X_test)
    test_acc = accuracy_score(y_test, y_pred)
    
    return {
        "10-Fold CV Accuracy": cv_mean,
        f"Acurácia {int((1 - test_size)*100)}/{int(test_size*100)}": test_acc
    }




def avaliacao_bagging(modelo, X, y, n_estimators=10, max_samples=1.0, max_features=1.0):
    bagging = BaggingClassifier(
        estimator=modelo,
        n_estimators=n_estimators,
        max_samples=max_samples,
        max_features=max_features,
        random_state=0
    )

    # 10-Fold Cross-Validation
    cv_scores = cross_val_score(bagging, X, y, cv=10, scoring='accuracy')
    cv_mean = cv_scores.mean()

    # Diferentes divisões treino-teste
    split_results = {}
    for test_size in test_sizes:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=0)
        bagging.fit(X_train, y_train)
        y_pred = bagging.predict(X_test)

        acc = accuracy_score(y_test, y_pred)

        split_name = f"{int((1-test_size)*100)}/{int(test_size*100)}"
        split_results[split_name] = {"Acurácia": acc}

    return {"10-Fold CV": cv_mean, **split_results}

def avaliacao_adaboost(base_estimator, X, y, n_estimators=10):  
    adaboost = AdaBoostClassifier(  
        estimator=base_estimator,  
        n_estimators=n_estimators,  
        random_state=2  
    )  

    # 10-Fold Cross-Validation  
    cv_scores = cross_val_score(adaboost, X, y, cv=10, scoring='accuracy')  
    cv_mean = cv_scores.mean()  

    # Diferentes divisões treino-teste  
    split_results = {}  
    for test_size in test_sizes:  
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=2)  
        adaboost.fit(X_train, y_train)  
        y_pred = adaboost.predict(X_test)  

        acc = accuracy_score(y_test, y_pred)  
        prec = precision_score(y_test, y_pred, average='weighted')

        split_name = f"{int((1-test_size)*100)}/{int(test_size*100)}"  
        split_results[split_name] = {"Acurácia": acc}  

    return {"10-Fold CV": cv_mean, **split_results}  




# Definindo os modelos base para AdaBoost  
modelos_base = {  
    "Árvore de Decisão": DecisionTreeClassifier(max_depth=1),  # Stump para AdaBoost  
    "Naive Bayes": GaussianNB()  
}  
test_sizes = [0.1, 0.2, 0.3]  # 90/10, 80/20, 70/30  
n_estimators_list = [10, 20]  # Valores a testar  

results_adaboost = {}  
for nome, modelo in modelos_base.items():  
    for n_estimators in n_estimators_list:  
        key = f"{nome} (n={n_estimators})"  
        results_adaboost[key] = avaliacao_adaboost(modelo, X, y, n_estimators=n_estimators)  




tabela_1 = {}
for nome_modelo, modelo in modelos_base.items():    
    tabela_1[nome_modelo] = avaliacao_bagging(modelo, X, y)


selector = SelectKBest(score_func=f_classif, k=3)
X_selected = selector.fit_transform(X, y)
tabela_2 = {}
for nome_modelo, modelo in modelos_base.items():
    tabela_2[nome_modelo] = avaliacao_bagging(modelo, X_selected, y)


main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')
"""
    GET => RECUPERAR DADOS, 
    POST => ENVIAR ALGO PARA SER SALVO OU EM ROTAS DE LOGIN, 
    PUT => ATUALIZAR OS DADOS,
    PATCH => ATUALIZAR OS DADOS,
    DELETE => APAGAR OS DADOS

"""
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        senha = request.form['senha']
        if autenticar_usuario(login, senha):
            session["usuario"] = {"login": login, "senha": senha}
            return redirect(url_for('main.home'))
        else:
            flash('Usuário ou senha inválidos.')
    return render_template('login.html')