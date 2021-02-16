var app = new Vue({
    el: '#app',
    data: {
        color: "green",
        text: "",
        checked: true,
        city: "",
        comment: null,
        comments: ["some existing comment... ",],
        errors: null,
    },

    methods: {
        onSubmit() {
            let new_comment = this.comment;
            if (new_comment) {
                this.comments.push(new_comment);
                this.comment = null;
                if (this.errors) {
                    this.errors = null;
                }
            } else {
                this.errors = "the comment field cannot be empty"
            }
        }
    },

    computed: {},


});