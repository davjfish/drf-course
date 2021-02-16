var app = new Vue({
    el: '#app',
    data: {
        lesson: 'events and methods',
        counter: 0
    },
    methods: {
        incrementCounter() {
            this.counter += 1;
            console.log(this.counter);
            if (this.counter >= 10) {
                alert("counter is equal to " + this.counter)
            }
        },
        overTheBox() {
            alert("over the box")
        },
    }
});