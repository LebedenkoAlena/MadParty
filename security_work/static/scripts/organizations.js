let formsCount = parseInt(document.querySelector("#django-data-forms-count").textContent)
let organizationID = parseInt(document.querySelector("#django-data-organization").textContent)
document.querySelector(".django-data").remove()

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

const organizations = Vue.createApp({
    delimiters: ["[[", "]]"],
    data() {
        return {
            currentForm: 0,
            formsCount,
            organizationID
        }
    },
    methods: {
        nextForm() {
            if (this.currentForm < this.formsCount - 1) {
                this.currentForm += 1

                let data = new FormData(document.querySelector("#activeForm"))
                axios.post(`http://127.0.0.1:8000/organization/edit/${this.organizationID}/${this.currentForm}`).then(response => {
                    console.log(response)
                })
            }
        },
        backForm() {
            if (this.currentForm > 0) {
                this.currentForm -= 1
            }
        }
    }
}).mount("#organizations")