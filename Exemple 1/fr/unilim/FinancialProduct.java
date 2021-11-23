package fr.unilim;
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