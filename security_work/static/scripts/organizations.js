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
    methods: {
        nextForm() {
            console.log(formsCount)
            if (this.currentForm < this.formsCount - 1) {
                this.currentForm += 1
            }
            console.log(this.currentForm)
        },
        backForm() {
            if (this.currentForm > 0) {
                this.currentForm -= 1
            }
        }
    }
}).mount("#organizations")