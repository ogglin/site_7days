let data = {
    categories: JSON.parse(document.getElementById('categoriesData').textContent),
    all_classys: JSON.parse(document.getElementById('classysData').textContent),
    lang: JSON.parse(document.getElementById('lang').textContent),
    projectID: 812923448506,
    clHeadRu: `<h4>Ищете работу? Хотите познакомиться? Хотите снять квартиру? Просмотрите наши объявления.
                    Ищете сотрудников? Хотите сдать квартиру в рент? Разместите свое объявление.</h4>
                <details>
                    <summary>Подать объявление</summary>
                    <h3>Правила подачи объявлений</h3>
                    <h4>Объявления можно подавать и оплачивать любым из следующих способов:</h4>
                    <ol>
                        <li>Заполните купон из газеты, вложите в конверт вместе с чеком или money order на имя Ethnic Media
                            и отправьте почтой по адресу: Ethnic Media, 25 Telser, P.O. Box 261, Lake Zurich, IL 60047
                            Отправьте объявление текстовым сообщением на номер 312-999-0609, в тексте укажите количество
                            выходов (сколько недель публиковать объявление) и Ваш контактный телефон. Сотрудник редакции
                            перезвонит Вам в течение ближайшего рабочего дня и примет оплату.
                        </li>
                        <li>Отправьте объявление по ЭЛЕКТРОННОЙ ПОЧТЕ на info@ethnicmedia.us, укажите количество выходов
                            (сколько недель публиковать объявление) и Ваш контактный телефон. Сотрудник редакции перезвонит
                            Вам в течение ближайшего рабочего дня и примет оплату.
                        </li>
                        <li>Отправьте текст объявления по факсу 866-710-0220, укажите количество выходов (сколько недель
                            публиковать объявление) и Ваш контактный телефон. Сотрудник редакции перезвонит Вам в течение
                            ближайшего рабочего дня и примет оплату.
                        </li>
                    </ol>
                    <h4>Общие правила для раздела “Объявления”</h4>
                    <ul>
                        <li>Стоимость объявления в одном номере газеты: 50¢ за слово.</li>
                        <li>Номер телефона считается как за одно слово.</li>
                        <li>Слова, выделенные жирными или ЗАГЛАВНЫМИ буквами: 60¢ за слово.</li>
                        <li>Если вы хотите поместить свое объявление в нескольких номерах, то сумму умножьте на количество
                            публикаций.
                        </li>
                        <li>Фотография в объявлении: $5.</li>
                        <li>Объявление в рамке: $5 за модуль (1”х1,5”)</li>
                    </ul>
                    <h4>Поздравление с праздником (день рождения, юбилей, свадьба) в рамке (текст и фотография) - от 10
                        долларов, в зависимости от размера объявления. Некрологи, соболезнования (текст и фотография),
                        публикуются БЕСПЛАТНО</h4>
                </details>`,
    clHeadEn: `<h4>Looking for a job? Would you like to meet me? Do you want to rent an apartment? View our ads.
                   Looking for employees? Do you want to rent an apartment? Place your ad.</h4>
                <details>
                    <summary>Подать объявление</summary>
                    <h3>Правила подачи объявлений</h3>
                    <h4>Объявления можно подавать и оплачивать любым из следующих способов:</h4>
                    <ol>
                        <li>Заполните купон из газеты, вложите в конверт вместе с чеком или money order на имя Ethnic Media
                            и отправьте почтой по адресу: Ethnic Media, 25 Telser, P.O. Box 261, Lake Zurich, IL 60047
                            Отправьте объявление текстовым сообщением на номер 312-999-0609, в тексте укажите количество
                            выходов (сколько недель публиковать объявление) и Ваш контактный телефон. Сотрудник редакции
                            перезвонит Вам в течение ближайшего рабочего дня и примет оплату.
                        </li>
                        <li>Отправьте объявление по ЭЛЕКТРОННОЙ ПОЧТЕ на info@ethnicmedia.us, укажите количество выходов
                            (сколько недель публиковать объявление) и Ваш контактный телефон. Сотрудник редакции перезвонит
                            Вам в течение ближайшего рабочего дня и примет оплату.
                        </li>
                        <li>Отправьте текст объявления по факсу 866-710-0220, укажите количество выходов (сколько недель
                            публиковать объявление) и Ваш контактный телефон. Сотрудник редакции перезвонит Вам в течение
                            ближайшего рабочего дня и примет оплату.
                        </li>
                    </ol>
                    <h4>Общие правила для раздела “Объявления”</h4>
                    <ul>
                        <li>Стоимость объявления в одном номере газеты: 50¢ за слово.</li>
                        <li>Номер телефона считается как за одно слово.</li>
                        <li>Слова, выделенные жирными или ЗАГЛАВНЫМИ буквами: 60¢ за слово.</li>
                        <li>Если вы хотите поместить свое объявление в нескольких номерах, то сумму умножьте на количество
                            публикаций.
                        </li>
                        <li>Фотография в объявлении: $5.</li>
                        <li>Объявление в рамке: $5 за модуль (1”х1,5”)</li>
                    </ul>
                    <h4>Поздравление с праздником (день рождения, юбилей, свадьба) в рамке (текст и фотография) - от 10
                        долларов, в зависимости от размера объявления. Некрологи, соболезнования (текст и фотография),
                        публикуются БЕСПЛАТНО</h4>
                </details>`
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
            lang: data.lang,
            clHead: data.clHeadRu,
            category_active: 0,
            categoryName: 'Все',
            isActive: false
        }
    },
    methods: {
        filterCat(id, name) {
            btns = document.getElementsByClassName('btn_cat')
            const clArr = []
            if (this.category_active === id) {
                this.classys = this.all_classys
                for (let i = 0; i < btns.length; i++) {
                    btns[i].classList.remove('active')
                }
                this.category_active = 0
                if (this.lang === 'ru') {
                    this.categoryName = 'Все'
                } else {
                    this.categoryName = 'All'
                }

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
        },
        changeLang() {
            if (this.lang === 'ru') {
                this.lang = 'en'
                this.clHead = data.clHeadEn
            } else {
                this.lang = 'ru'
                this.clHead = data.clHeadRu
            }
        }
    }
}).mount('#app');

