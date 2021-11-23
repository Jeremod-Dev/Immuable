package fr.unilim;
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