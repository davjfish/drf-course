var app = new Vue({
    el: '#app',
    data: {
        is_circle: true,
        styleObject: {backgroundColor: 'green', border: '5px solid orange'},
    },
    methods: {
        changeShape(){
            this.is_circle = !this.is_circle
        }
    }
});