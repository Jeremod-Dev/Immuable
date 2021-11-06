# Qu'est ce qu'un Design Pattern

Le terme de Design Pattern est apparue suite à la publication du livre *Design Patterns* par Gamma, Helm, Johnson et Vlissides en 1994. Il presente une solution à un probleme de conception dans le paradigme de programmation orienté objet. Les Design Patterns montre la solution au probleme et explique comment mettre en oeuvre la solution.

 Au debut de leur ouvrage, le Gand of Four - surnom donné aux auteurs de l'ouvrage *Design Patterns* - mettent en avant les principes de Gamma. Le premier principe explicite qu'il est préconisé et plus fiable de programmer vers une interface. Le développeur devrait programmer grace à des interfaces et non directement avec l'objet en question. Finalement, le developpeur ne doit se soucié uniquement des communications avec l'objet - ce qu'il peut envoyer et recevoir - et non l'objet qui se cache derrière. Le deuxieme principe est la délégation du code qui permet la réutilisation de morceau de code. L'objet principal envoi une requète à un seconde objet - Le délégué - qui va transmettre la requete à l'objet recepteur. Ainsi dans ce processus, la communication va passer par trois acteurs dont un qui vient aidé l'emetteur.

Finalement, dans l'ouvrage, *Design Patterns*, est présenté un nombre de Designe Patterns car bien que des modèles généralisé, il n'est pas toujours nécessaire et pertinant d'utiliser un design plutot qu'un autre. Par ailleurs, les designes proposé sont classés en catégories dont en voici quelques une - modèle de Gof -:

- <u>Creational Pattern</u> - modèle de création: Permet une optimisation de la création des objets
- <u>Structural Pattern</u> - modèle de structuration: Permet de faire une suite de classe
- <u>Behavioral patterns</u> - modèle de Comportement: Permet d'apporter des solutions à des problèmes recurrent programmation informatique. 

# Mise en situation - Achat sur une place boursière

**Contexte:** Vous êtes un boursicoteur qui souhaite acheter des produits financiers sur un marché. Pour passer vos ordres d'achat vous faites appel à un courtier, qui s'occupera d'effectuer votre achat. Attention, vous êtes un petit nouveau dans le domaine et vous ne voulez pas prendre trop de risque - le marché étant très liquide -. Ainsi, vous passez votre ordre avec un cours limité, c'est-à-dire que vous donnez le prix maximum pour lequel vous souhaitez acheter votre titre. Au delà, votre ordre ne sera pas effectué. 

Voici la classe `Broker` qui correspond à votre courtier
```java
public class Broker {
    private Integer stoploss;

    public Broker(Integer stoploss) {
        this.stoploss = stoploss;
    }
    public Integer getStoploss() {
        return stoploss;
    }
    public void setStoploss(Integer stoploss) {
        this.stoploss = stoploss;
    }
    @Override
    public String toString() {
        return ""+stoploss ;
    }
}
```
Ici la class `FinancialProduct` correspond au produit financier que vous souhaitez acheter
```java
public class FinancialProduct{
    private String name;
    private String type;
    private Broker stopLoss;

    public FinancialProduct(String name, String type, Broker stopLoss) {
        this.name = name;
        this.type = type;
        this.stopLoss = stopLoss;
    }

    @Override
    public String toString() {
        return "Order Buy{" +
                "name='" + name + '\'' +
                ", type='" + type + '\'' +
                ", stopLoss=" + stopLoss +
                '}';
    }
}
```
Présentement, vous allez demander à votre `Broker` de passer un ordre d'achat d`'action` à cours limité - stopLoss - à `1200€`, sur la firme `Tesla`.

```java
public class Main {
    public static void main(String[] args) {
        Broker broker = new Broker(1200);
        FinancialProduct order1 = new FinancialProduct("Tesla", "action", broker);
        System.out.println(order1 + "\n");
    }
}
```
Une fois cela fait votre courtier vous affiches les détails de l'ordre.
```
Order Buy{name='Tesla', type='action', stopLoss=1200}
```

Cela fait vous decidez de passer un second ordre d'achat d'`action` avec un cours limité à `290€` cette fois-ci, sur l'entreprise `Meta`.

```Java
public class Main {
    public static void main(String[] args) {
        Broker broker = new Broker(1200);
        FinancialProduct order1 = new FinancialProduct("Tesla", "action", broker);
        System.out.println(order1 + "\n");

        broker.setStoploss(290);
        FinancialProduct order2 = new FinancialProduct("Meta", "action", broker);

        System.out.println(order1);
        System.out.println(order2);
    }
}
```
Une fois cela fait, le courtier vous affiches les détails de vos ordres d'achat..
```
Order Buy{name='Tesla', type='action', stopLoss=290}
Order Buy{name='Meta', type='action', stopLoss=290}
```
Mince, il y a une erreur dans les details de l'ordre sur `Tesla`! :unamused:


[markdowns/welcome.md](https://github.com/TechDotIO/techio-basic-template/blob/master/markdowns/welcome.md)
What you are reading here is generated by this file. Tech.io uses the [Markdown syntax](https://tech.io/doc/reference-markdowns) to render text, media and to inject programming exercises.


[techio.yml](https://github.com/TechDotIO/techio-basic-template/blob/master/techio.yml)
This mandatory file describes both the table of content and the programming project(s). The file path should not be changed.