// comment list component
Vue.component("comment-list", {
    props: {
        comments: {
            type: Array,
            required: true,
        }
    },
    data: function () {
        return {
            new_comment: null,
            comment_author: null,
            errors: null
        }
    },
    methods:{
        submitComment(){
            if(this.new_comment && this.comment_author) {
                this.$emit('submit-comment',{username: this.comment_author, content: this.new_comment});
                this.comment_author = null;
                this.new_comment = null;
                if(this.errors) {
                    this.errors = null;
                }
            } else {
                this.errors = "";
                if(!this.comment_author) {
                    this.errors += "You must enter a author name; ";
                }
                if (!this.new_comment){
                    this.errors += "You must enter a comment";
                }
            }

        }
    },
    template: `
        <div class="container">
                <div class="mt-3">
                    <single-comment v-for="(comment, index) in comments"
                             :comment="comment"
                             :key="index">
                    </single-comment>
                </div>
                <hr>
                <h3 v-if="errors"> {{errors}}</h3>
                <form @submit.prevent="submitComment">
                    <div class="form-group">
                    <label for="commentAuthor">Your Username</label>
                    <input type="text" id="commentAuthor" class="form-control" v-model="comment_author">
                    </div>
                    <div class="form-group">
                        <label for="commentText">Your Comment</label>
                        <textarea class="form-control" id="commentText" cols="30" rows="10" v-model="new_comment"></textarea>
                    </div>
                    <button type="submit" class="btn btn-sm btn-primary">Publish</button>
                </form>
        </div>
    `
});


// single comment component
Vue.component("single-comment", {
    props: {
        comment: {
            type: Object,
            required: true,
        }
    },
    template: `
        <div class="card mb-3" style="width: 18rem;">
            <div class="card-header">
                <p class="card-text">Published by: {{comment.username}}</p>
            </div>
            <div class="card-body">
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
    methods: {
        addNewComment(new_comment){
            this.comments.push(new_comment);
        }
    }
});