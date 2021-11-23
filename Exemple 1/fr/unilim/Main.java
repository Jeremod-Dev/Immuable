package fr.unilim;
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