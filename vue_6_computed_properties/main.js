var app = new Vue({
    el: '#app',
    data: {
        title: "Computed Properties",
        first_name: "john",
        last_name: "doe",
    },
    methods: {
        getRandomNumber(){
            return Math.random()
        }
    },
    computed: {
        getRandomComputed(){
            return Math.random()
        },
        fullName(){
            return `${this.first_name} ${this.last_name}`;
        },
        reversedFullName(){
            first = this.first_name.split("").reverse().join("");
            last = this.last_name.split("").reverse().join("");
            return `${first} ${last}`;
        },
    },


});