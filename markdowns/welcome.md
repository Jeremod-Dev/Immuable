# Qu'est ce qu'un Design Pattern

Le terme de Design Pattern est apparue suite à la publication d'un Essai de C. Alexander en 1977, *A Pattern Language: Towns, Buildings, Construction*. Cette notion a par la suite été repris dans l'ouvrage *Design Patterns* par Gamma, Helm, Johnson et Vlissides en 1994. Il presente une solution à un probleme de conception dans le paradigme de programmation orienté objet. Les Design Patterns montre la solution au probleme concerné et explique comment mettre en oeuvre la solution.

 Au début de leur ouvrage, le Gand of Four - surnom donné aux auteurs de l'ouvrage *Design Patterns* - mettent en avant les principes de Gamma. Le premier principe explicite qu'il est préconisé et plus fiable de programmer vers une interface. Le développeur devrait programmer grace à des interfaces et non directement avec l'objet en question. Finalement, le developpeur ne doit se soucié uniquement des communications avec l'objet - ce qu'il peut envoyer et recevoir - et non l'objet qui se cache derrière. Le deuxieme principe est la délégation du code qui permet la réutilisation de morceau de code. L'objet principal envoi une requète à un seconde objet - Le délégué - qui va transmettre la requete à l'objet recepteur. Ainsi dans ce processus, la communication va passer par trois acteurs dont un qui vient aidé l'emetteur.

Finalement, dans l'ouvrage, *Design Patterns*, est présenté un nombre de Designe Patterns car bien que des modèles généralisé, il n'est pas toujours nécessaire et pertinant d'utiliser un design plutot qu'un autre. Par ailleurs, les designes proposé sont classés en catégories - modèle de Gof -:

- <u>Creational Pattern</u> - modèle de création: Permet une optimisation de la création des objets
- <u>Structural Pattern</u> - modèle de structuration: Permet de faire une suite de classe
- <u>Behavioral patterns</u> - modèle de Comportement: Permet d'apporter des solutions à des problèmes recurrent programmation informatique. 

# Mise en situation - Achat sur une place boursière

**Contexte:** Vous êtes un boursicoteur qui souhaite acheter des produits financiers sur un marché. Pour passer vos ordres d'achat vous faites appel à un courtier, qui s'occupera de les effectuer à votre place. Attention, vous êtes un petit nouveau dans le domaine et vous ne voulez pas prendre trop de risque - le marché étant très liquide -. Ainsi, vous passez votre ordre avec un cours limité avec un stopLoss.

Ici la classe `FinancialProduct` correspond au produit financier que vous souhaitez acheter
```java
public class FinancialProduct{
    private Criteria criteria;
    private int stopLoss;

    public FinancialProduct(Criteria criteria, int stopLoss) {
        this.criteria = criteria;
        this.stopLoss = stopLoss;
    }

    @Override
    public String toString() {
        return "Order Buy{" +
                "name='" + criteria.getName() + '\'' +
                ", type='" + criteria.getType() + '\'' +
                ", stopLoss=" + stopLoss +
                '}';
    }
}
```
Le produit financier admet differents critères qui sont dans la classe `Criteria`
```java
public class Criteria {
    private String name;
    private String type;

    public Criteria(String name, String type) {
        this.name = name;
        this.type = type;
    }

    public void setCriteria(String name, String type) {
        this.name = name;
        this.type = type;
    }

    public String getType() {
        return type;
    }
    public String getName() {
        return name;
    }
}
```

Présentement, vous allez demander à votre `Broker` de passer un ordre d'achat d`'action` à cours limité - stopLoss - à `1200€`, sur la firme `Tesla`.

```java
public class Main {
    public static void main(String[] args) {
        Criteria criteria = new Criteria("Tesla", "Action");

        FinancialProduct order1 = new FinancialProduct(criteria, 1200);
        System.out.println(order1 + "\n");
    }
}
```
Une fois cela fait votre courtier vous affiches les détails de l'ordre.
```
Order Buy{name='Tesla', type='Action', stopLoss=1200}
```

Cela fait, vous decidez de passer un second ordre d'achat d'`Obligation` avec un cours limité à `290€` cette fois-ci, sur l'entreprise `Meta`.

```Java
public class Main {
    public static void main(String[] args) {
        Criteria criteria = new Criteria("Tesla", "Action");

        FinancialProduct order1 = new FinancialProduct(criteria, 1200);
        System.out.println(order1 + "\n");

        criteria.setCriteria("Meta", "Obligation");
        FinancialProduct order2 = new FinancialProduct(criteria, 290);

        System.out.println(order1);
        System.out.println(order2);
    }
}
```
Une fois cela fait, le courtier vous affiches les détails de vos ordres d'achat..
```
Order Buy{name='Meta', type='Action', stopLoss=1200}
Order Buy{name='Meta', type='Action', stopLoss=290}
```
Mince... les critères du titre financier du premier ordre ne sont plus bon! 😒

![Diagramme De classe](https://github.com/Jeremod-Dev/DesignPattern/blob/master/markdowns/Diagramme_classe0.PNG)

## Résolution du problème

Dans notre cas, le premier affichage est correct, mais le second est mauvais car l'on a modifier les critères du produit financier. Pour résoudre cet embrouillamini il suffirait de créer une nouvelle instance de l'objet `Critéria`! 😃
```java
public class Main {
    public static void main(String[] args) {
        Criteria criteria1 = new Criteria("Tesla", "Action");

        FinancialProduct order1 = new FinancialProduct(criteria1, 1200);
        System.out.println(order1 + "\n");

         Criteria criteria2 = new Criteria("Meta", "Obligation");
        FinancialProduct order2 = new FinancialProduct(criteria2, 290);

        System.out.println(order1);
        System.out.println(order2);
    }
}
```
Cette fois-ci l'affichage est correct ! 😄
```
Order Buy{name='Tesla', type='Action', stopLoss=1200}
Order Buy{name='Meta', type='Action', stopLoss=290}
```

Notre problème est résolu temporairement... si un utilisateur du programme vient à modifier les critères plutôt que de recréer une instance, il créera un bug dans le programme. Il ne faut jamais faire confiance à un utilisateur. 😒

Nous allons faire en sorte que l'objet `Criteria` ne puisse plus être modifier après sa création. Pour cela, nous enlevons les `setteur` et les attributs de la classe en `final`.

Voici la classe `Criteria` après ces modificaitons.
```java
public class Criteria {
    private final String name;
    private final String type;

    public Criteria(String name, String type) {
        this.name = name;
        this.type = type;
    }

    public String getType() {
        return type;
    }
    public String getName() {
        return name;
    }
}
```

![Diagramme De classe](https://github.com/Jeremod-Dev/DesignPattern/blob/master/markdowns/Diagramme_classe.PNG)

En Java 14, il est possible de créer un objet qui ne sera jamais modifier après sa création grace au mot-clef `record`.

Notre classe `Criteria` devient alors ceci
```java
public record Criteria(String name, String type) {

    public String getType() {
        return type;
    }

    public String getName() {
        return name;
    }
}
```
avec le diagramme de classe suivant:
![Diagramme De classe](https://github.com/Jeremod-Dev/DesignPattern/blob/master/markdowns/Diagramme_calsse1.PNG)
Nous avons utilisé ici, sans le savoir, un design pattern nommée `immutable`

[markdowns/welcome.md](https://github.com/TechDotIO/techio-basic-template/blob/master/markdowns/welcome.md)
What you are reading here is generated by this file. Tech.io uses the [Markdown syntax](https://tech.io/doc/reference-markdowns) to render text, media and to inject programming exercises.


[techio.yml](https://github.com/TechDotIO/techio-basic-template/blob/master/techio.yml)
This mandatory file describes both the table of content and the programming project(s). The file path should not be changed.