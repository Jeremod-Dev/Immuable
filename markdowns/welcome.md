# Qu'est ce qu'un Design Pattern

Le terme de *design pattern* est apparue suite à la publication d'un essai de C. Alexander en 1977, *A Pattern Language: Towns, Buildings, Construction*. Cette notion a par la suite été repris dans l'ouvrage *Design Patterns* par Gamma, Helm, Johnson et Vlissides en 1994. Il présente une solution à un problème de conception dans le paradigme de programmation orienté objet. Les design patterns montrent la solution aux problèmes concernés et expliquent comment mettre en oeuvre la solution.

 Au début de leur ouvrage, le Gang of Four - surnom donné aux auteurs de l'ouvrage *Design Patterns* - met en avant les principes de Gamma. Le premier principe explicite qu'il est préconisé et plus fiable de programmer vers une interface. Le développeur devrait programmer grâce à des interfaces et non directement avec l'objet en question. Finalement, le développeur ne doit se soucier uniquement des communications avec l'objet - ce qu'il peut envoyer et recevoir - et non l'objet qui se cache derrière. Le deuxieme principe est la délégation du code qui permet la réutilisation de morceau de code. L'objet principal envoie une requête à un second objet - le délégué - qui va transmettre la requête à l'objet récepteur. Ainsi dans ce processus, la communication va passer par trois acteurs dont un qui vient aider l'émetteur.

Finalement, dans l'ouvrage, *Design Patterns*, sont présentés un certain nombre de design patterns car bien que ce soit des modèles généralisés, il n'est pas toujours nécessaire et pertinent d'utiliser un design plutôt qu'un autre. Par ailleurs, les designs proposés sont classés en catégories - modèle de Gof -:

- <u>Creational Pattern</u> - modèle de création: Permet une optimisation de la création des objets
- <u>Structural Pattern</u> - modèle de structuration: Permet d'augmenter la fonctionnalité des objets, sans modifier leur composition
- <u>Behavioral patterns</u> - modèle de Comportement: Conçus en fonction de la façon avec laquelle les classes communiquent entre elles


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
Le produit financier admet différents critères qui sont dans la classe `Criteria`
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
Une fois cela fait votre courtier vous affiche les détails de l'ordre.
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
Order Buy{name='Meta', type='Obligation', stopLoss=1200}
Order Buy{name='Meta', type='Obligation', stopLoss=290}
```
Mince... les critères du titre financier du premier ordre ne sont plus bon! 😒

![Diagramme De classe](https://siteedt.000webhostapp.com/Diagramme_classe0.PNG)

## Résolution du problème

Dans notre cas, le premier affichage est correct, mais le second est mauvais car l'on a modifié les critères du produit financier. Pour résoudre cet embrouillamini il suffirait de créer une nouvelle instance de l'objet `Critéria`! 😃
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
Order Buy{name='Meta', type='Obligation', stopLoss=290}
```

Notre problème est résolu temporairement... si un utilisateur du programme vient à modifier les critères plutôt que de recréer une instance, il créera un bug dans le programme. Il ne faut jamais faire confiance à un utilisateur. 😒

Nous allons faire en sorte que l'objet `Criteria` ne puisse plus être modifier après sa création. Pour cela, nous enlevons les `setteur` et les attributs de la classe et la classe en `final`.

Voici la classe `Criteria` après ces modificaitons.
```java
public final class Criteria {
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

![Diagramme De classe](https://siteedt.000webhostapp.com/Diagramme_classe.PNG)

En Java 14, il est possible de créer un objet qui ne sera jamais modifié après sa création grâce au mot-clé `record`.

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

![Diagramme De classe](https://siteedt.000webhostapp.com/Diagramme_calsse1.PNG)

Nous avons utilisé ici, sans le savoir, un design pattern nommée `immutable`

## Présentation du Design Pattern Immutable
Ce design propose de créer une nouvelle instance de l'objet plutôt que de modifier la classe. Ainsi il faut protéger la classe.

Ce design appartient à la catégorie des designs `concurrent`.

## Les Avantages de l'immuabilité

Les classes immuables ont des avantages:

- Thread-safe et fortement conseillé dans un environnement en multithread
- Facilement lisible car elle n'admet pas de méthode de modification
- Constructeur n'est pas nécéssaire. 

## Les Limites de l'immuabilité

Les classes immuables ont des inconvénients:
- Création de nouvelles instances (coûteux en mémoire)
- Utilisation peu fréquentes.

## Le lien avec les principes SOLID

Dans le paradygme de programmation orienté objet, il existe 5 principes de conception architectural. Ces principes sont réunis dans l'acrynome SOLID

S - **Single Responsibility Principle:** Une responsabilité par classe

O - **Open Closed Principle:** Ouverture aux implémentations et fermé aux modifications

L - **Liskov Substitution Principle:** Les sous-types doivent pouvoir être substitué à leur type de base.

I - **Interface segregation Principle:** Préférer plusieurs interfaces spécifiques plutôt qu'une seule générale

D - **Dependency Inversion Principle:** Les objets de haut niveau ne doivent pas dépendre des objets de bas niveau

Le fait est, ici, que la classe immuable est simplement une classe plus restrictive mais il est possible de concevoir un programme qui respecte tous ces principes.

#### Lien vers le github

https://github.com/Jeremod-Dev/Immuable.git

## Réferences utilisées

https://gfx.developpez.com/tutoriel/java/immuables/#LII

https://wodric.com/classe-immutable/

https://lkumarjain.blogspot.com/2016/02/immutable-design-pattern.html

https://springframework.guru/gang-of-four-design-patterns/

https://fr.wikipedia.org/wiki/Objet_immuable