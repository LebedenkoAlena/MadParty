let formsCount = parseInt(document.querySelector("#django-data-forms-count").textContent)
document.querySelector(".django-data").remove()

const organizations = Vue.createApp({
    delimiters: ["[[", "]]"],
    data() {
        return {
            currentForm: 0,
            formsCount
        }
    },
    mounted() {
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
        axios.defaults.xsrfCookieName = "csrftoken";
        axios.post("http://127.0.0.1:8000/login/", {
            data: {
                username: "admin",
                password: "qwerty123"
            }
        }).then(response => {
            console.log(response)
        })
    },
    methods: {
        nextForm() {
            if (this.currentForm < this.formsCount - 1) {
                this.currentForm += 1
            }
        },
        backForm() {
            if (this.currentForm > 0) {
                this.currentForm -= 1
            }
        }
    }
}).mount("#organizations")