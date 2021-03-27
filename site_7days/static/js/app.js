let data = {
    categories: JSON.parse(document.getElementById('categoriesData').textContent),
    all_classys: JSON.parse(document.getElementById('classysData').textContent),
}

const app = Vue.createApp({
    data() {
        const cats = []
        data.categories.forEach(cat => {
            data.all_classys.forEach(cl => {
                if (cat.id === cl.categories_id) {
                    if (cats.indexOf(cat) < 0) {
                        cats.push(cat)
                    }
                }
            })
        });
        return {
            all_classys: data.all_classys,
            categories: cats,
            classys: data.all_classys,
            category_active: 0,
            categoryName: 'Все',
            isActive: false
        }
    },
    methods: {
        filterCat(id, name) {
            console.log(id)
            btns = document.getElementsByClassName('btn_cat')
            const clArr = []
            if (this.category_active === id) {
                this.classys = this.all_classys
                for (let i = 0; i < btns.length; i++) {
                    btns[i].classList.remove('active')
                }
                this.category_active = 0
                this.categoryName = 'Все'
            } else {
                this.all_classys.forEach(el => {
                    if (el['categories_id'] === id) {
                        clArr.push(el)
                    }
                })
                this.classys = clArr;
                for (let i = 0; i < btns.length; i++) {
                    btns[i].classList.remove('active')
                }
                document.getElementById('btn_cat' + id).className = "btn_cat active"
                this.category_active = id
                this.categoryName = name
            }
        },
        showCats() {
            if (document.getElementById('aside').className === 'active') {
                document.getElementById('aside').className = ''
            } else {
                document.getElementById('aside').className = 'active'
            }
        }
    }
}).mount('#app');

