// to-do list
Vue.component("to-do", {
    props: {
        tasks: {
            type: Array,
            required: true,
        },
        count: {
            type: Number,
            required: true,
        },
    },
    data: function () {
        return {
            new_task: null,
        }
    },

    methods: {
        submitTask() {
            if (this.new_task) {
                this.$emit('submit-new-task', this.new_task);
                this.new_task = null;
            }
        },
        removeTask(index) {
            this.$emit('remove-task', index);
        }
    },
    template: `
        <div class="container">
            <p class="font-weight-bold">Remaining Tasks: {{ count }}</p>
            <form @submit.prevent="submitTask">
                <div class="form-group">
                    <input type="text" class="form-control" placeholder="What do you need to do?" v-model="new_task">
                </div>
            </form>
            <p v-if="!count">To add a new task, write something and press enter</p>
            
            <single-task v-for="(task, index) in tasks"
                     :task="task"
                     :key="index"
                     :index="index"
                     @remove-task="removeTask(index)"
                     >
            </single-task>
        </div>


    `
});

// single task
Vue.component("single-task", {
    props: {
        task: {
            type: String,
            required: true,
        },
        index: {
            type: Number,
            required: true,
        },

    },
    methods: {
        removeTask() {
            this.$emit('remove-task');
        }
    },
    template: `
        <div class="alert alert-success alert-dismissible fade show" role="alert">
            <p class="my-0"> {{ task }}</p>
            <button @click="removeTask" type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        </div>
    `
});


var app = new Vue({
    el: '#app',
    data: {
        task: null,
        tasks: []
    },
    methods: {
        addNewTask(new_task) {
            this.tasks.push(new_task);
        },
        removeTask(index) {
            this.tasks.splice(index, 1);
        }
    },
    computed: {
        taskCount() {
            return this.tasks.length
        }
    }
});