Vue.component("comment", {
    props: {
        comment: {
            type: Object,
            required: true,
        }
    },
    template: `
        <div class="card" style="width: 18rem;">
            <div class="card-body">
                <p class="card-text">{{comment.username}}</p>
                <p class="card-text">{{comment.content}}</p>
            </div>
        </div>
    `
});


var app = new Vue({
    el: '#app',
    data: {
        comments: [
            {username: "alice", content: "first comment!"},
            {username: "bob", content: "ola!"},
            {username: "carole", content: "hello world!"},
            {username: "ted", content: "last comment :("},
        ]
    },
    methods: {}
});