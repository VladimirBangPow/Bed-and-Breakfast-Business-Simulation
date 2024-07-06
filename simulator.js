// Property class
class Property {
    constructor({ name, price, downPayment, interestRate, loanTerm, cleaningCost, rentalIncome, managementCost }) {
        this.name = name;
        this.price = price;
        this.downPayment = downPayment;
        this.interestRate = interestRate;
        this.loanTerm = loanTerm;
        this.cleaningCost = cleaningCost;
        this.rentalIncome = rentalIncome;
        this.managementCost = managementCost;
        this.remainingDebt = price - downPayment;
        this.mortgage = this.calculateMonthlyMortgage();
        this.propertyTax = this.calculateYearlyPropertyTax();
    }

    // Calculate the monthly mortgage payment
    calculateMonthlyMortgage() {
        const loanPrincipal = this.price - this.downPayment;
        const monthlyInterestRate = this.interestRate / 12 / 100;
        const numberOfPayments = this.loanTerm * 12;
        return loanPrincipal * (monthlyInterestRate * Math.pow(1 + monthlyInterestRate, numberOfPayments)) / (Math.pow(1 + monthlyInterestRate, numberOfPayments) - 1);
    }

    // Calculate the yearly property tax
    calculateYearlyPropertyTax() {
        const taxRate = 0.015; // 1.5% property tax rate
        return this.price * taxRate;
    }

    // Simulate one year of expenses and income
    simulateYear() {
        const yearlyMortgage = this.mortgage * 12;
        const yearlyTax = this.propertyTax;
        const yearlyCleaning = this.cleaningCost * 12;
        const yearlyManagement = this.managementCost * 12;
        const yearlyIncome = this.rentalIncome * 12;

        this.remainingDebt -= yearlyMortgage;

        return {
            income: yearlyIncome,
            expenses: yearlyMortgage + yearlyTax + yearlyCleaning + yearlyManagement,
            remainingDebt: this.remainingDebt,
            equity: this.price - this.remainingDebt
        };
    }
}

// Airbnb Business Simulator
class AirbnbBusinessSimulator {
    constructor() {
        this.properties = [];
        this.yearlyData = [];
        this.propertyCounter = 0;
        this.initialPropertyParams = null;
        this.cashBalance = 0;
        this.cashWithholdPercentage = 0;
    }

    setCashWithholdPercentage(percentage) {
        this.cashWithholdPercentage = percentage;
    }

    addProperty({ price, downPayment, interestRate, loanTerm, cleaningCost, rentalIncome, managementCost }) {
        const property = new Property({
            name: `Property ${++this.propertyCounter}`,
            price,
            downPayment,
            interestRate,
            loanTerm,
            cleaningCost,
            rentalIncome,
            managementCost
        });
        this.properties.push(property);
        if (!this.initialPropertyParams) {
            this.initialPropertyParams = { price, downPayment, interestRate, loanTerm, cleaningCost, rentalIncome, managementCost };
        }
    }

    simulateYears(years) {
        for (let year = 1; year <= years; year++) {
            let totalIncome = 0;
            let totalExpenses = 0;
            let totalDebt = 0;
            let totalEquity = 0;

            this.properties.forEach(property => {
                const { income, expenses, remainingDebt, equity } = property.simulateYear();
                totalIncome += income;
                totalExpenses += expenses;
                totalDebt += remainingDebt;
                totalEquity += equity;
            });

            // Calculate the yearly profit and adjust for cash withholding
            let yearlyProfit = totalIncome - totalExpenses;
            if (this.cashWithholdPercentage > 0) {
                const withheldAmount = yearlyProfit * this.cashWithholdPercentage / 100;
                yearlyProfit -= withheldAmount;
                this.cashBalance += withheldAmount;
            }

            // Calculate how many new properties can be bought with the profits
            const { price, downPayment, interestRate, loanTerm, cleaningCost, rentalIncome, managementCost } = this.initialPropertyParams;
            const newPropertiesCount = Math.floor(yearlyProfit / downPayment);

            for (let i = 0; i < newPropertiesCount; i++) {
                this.addProperty({
                    price,
                    downPayment,
                    interestRate,
                    loanTerm,
                    cleaningCost,
                    rentalIncome,
                    managementCost
                });
                yearlyProfit -= downPayment;
            }

            this.yearlyData.push({
                year,
                totalIncome,
                totalExpenses,
                totalDebt,
                propertiesCount: this.properties.length,
                cashBalance: this.cashBalance,
                totalEquity: totalEquity
            });
        }
    }

    // Generate Chart Data
    generateChartData(type) {
        switch (type) {
            case 'income':
                return {
                    labels: this.yearlyData.map(data => `Year ${data.year}`),
                    datasets: [{
                        label: 'Total Income',
                        data: this.yearlyData.map(data => data.totalIncome),
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
                    }]
                };
            case 'expenses':
                return {
                    labels: this.yearlyData.map(data => `Year ${data.year}`),
                    datasets: [{
                        label: 'Total Expenses',
                        data: this.yearlyData.map(data => data.totalExpenses),
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 1
                    }]
                };
            case 'debt':
                return {
                    labels: this.yearlyData.map(data => `Year ${data.year}`),
                    datasets: [{
                        label: 'Total Debt',
                        data: this.yearlyData.map(data => data.totalDebt),
                        backgroundColor: 'rgba(54, 162, 235, 0.2)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 1
                    }]
                };
            case 'properties':
                return {
                    labels: this.yearlyData.map(data => `Year ${data.year}`),
                    datasets: [{
                        label: 'Number of Properties',
                        data: this.yearlyData.map(data => data.propertiesCount),
                        backgroundColor: 'rgba(153, 102, 255, 0.2)',
                        borderColor: 'rgba(153, 102, 255, 1)',
                        borderWidth: 1
                    }]
                };
            case 'cash':
                return {
                    labels: this.yearlyData.map(data => `Year ${data.year}`),
                    datasets: [{
                        label: 'Cash Balance',
                        data: this.yearlyData.map(data => data.cashBalance),
                        backgroundColor: 'rgba(255, 206, 86, 0.2)',
                        borderColor: 'rgba(255, 206, 86, 1)',
                        borderWidth: 1
                    }]
                };
            case 'equity':
                return {
                    labels: this.yearlyData.map(data => `Year ${data.year}`),
                    datasets: [{
                        label: 'Total Equity',
                        data: this.yearlyData.map(data => data.totalEquity),
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
                    }]
                };
            case 'summary':
                return {
                    labels: ['Total Income', 'Total Expenses', 'Total Debt', 'Total Equity'],
                    datasets: [{
                        label: 'Summary',
                        data: [
                            this.yearlyData.reduce((sum, data) => sum + data.totalIncome, 0),
                            this.yearlyData.reduce((sum, data) => sum + data.totalExpenses, 0),
                            this.yearlyData.reduce((sum, data) => sum + data.totalDebt, 0),
                            this.yearlyData[this.yearlyData.length - 1].totalEquity
                        ],
                        backgroundColor: [
                            'rgba(75, 192, 192, 0.2)',
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(153, 102, 255, 0.2)'
                        ],
                        borderColor: [
                            'rgba(75, 192, 192, 1)',
                            'rgba(255, 99, 132, 1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(153, 102, 255, 1)'
                        ],
                        borderWidth: 1
                    }]
                };
            default:
                return {};
        }
    }

    // Render Chart
    renderChart(type, elementId) {
        const ctx = document.getElementById(elementId).getContext('2d');
        const chartType = type === 'summary' ? 'pie' : 'line';
        new Chart(ctx, {
            type: chartType,
            data: this.generateChartData(type),
            options: {
                scales: type !== 'summary' ? {
                    y: {
                        beginAtZero: true
                    }
                } : {}
            }
        });
    }

    renderAllCharts() {
        this.renderChart('income', 'incomeChart');
        this.renderChart('expenses', 'expensesChart');
        this.renderChart('debt', 'debtChart');
        this.renderChart('properties', 'propertiesChart');
        this.renderChart('cash', 'cashChart');
        this.renderChart('equity', 'equityChart');
        this.renderChart('summary', 'summaryChart');
    }
}

// Function to generate reports based on input values
function generateReports() {
    const price = parseFloat(document.getElementById('price').value);
    const downPayment = parseFloat(document.getElementById('downPayment').value);
    const interestRate = parseFloat(document.getElementById('interestRate').value);
    const loanTerm = parseInt(document.getElementById('loanTerm').value);
    const cleaningCost = parseFloat(document.getElementById('cleaningCost').value);
    const rentalIncome = parseFloat(document.getElementById('rentalIncome').value);
    const managementCost = parseFloat(document.getElementById('managementCost').value);
    const cashWithholdPercentage = parseFloat(document.getElementById('cashWithholdPercentage').value);

    const simulator = new AirbnbBusinessSimulator();
    simulator.addProperty({
        price,
        downPayment,
        interestRate,
        loanTerm,
        cleaningCost,
        rentalIncome,
        managementCost
    });

    simulator.setCashWithholdPercentage(cashWithholdPercentage);

    simulator.simulateYears(10);
    simulator.renderAllCharts();
}
