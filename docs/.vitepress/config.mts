import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "Гараж знаний",
  description: "Всё об автомобилях: выбор, обслуживание, налоги и законы",
  lang: 'ru-RU',
  
  themeConfig: {
    nav: [
      { text: 'Главная', link: '/' },
      { text: 'Подбор авто', link: '/selection/' },
      { text: 'Обслуживание', link: '/service/' },
      { text: 'Документы', link: '/docs/' }
    ],

    sidebar: {
      '/selection/': [
        {
          text: 'Подбор по бюджету',
          items: [
            { text: 'До 100 000 ₽', link: '/selection/budget-100' },
            { text: '100 000 - 200 000 ₽', link: '/selection/budget-200' },
            { text: '300 000 - 500 000 ₽', link: '/selection/budget-500' },
            { text: '500 000 - 1 000 000 ₽', link: '/selection/budget-1000' }
          ]
        }
      ],
      '/service/': [
        {
          text: 'Техническая часть',
          items: [
            { text: 'Устройство автомобиля', link: '/service/device' },
            { text: 'Техобслуживание для новичков', link: '/service/to-basics' },
            { text: 'Что проверять перед покупкой', link: '/service/checking' }
          ]
        }
      ],
      '/docs/': [
        {
          text: 'Документы и законы',
          items: [
            { text: 'Регистрация в ГИБДД', link: '/docs/registration' },
            { text: 'Транспортный налог', link: '/docs/tax' },
            { text: 'ОСАГО и Каско', link: '/docs/insurance' }
          ]
        }
      ],
      '/': [
        {
          text: 'Быстрый старт',
          items: [
            { text: 'О проекте', link: '/about' },
            { text: 'Связаться с нами', link: '/contacts' }
          ]
        }
      ]
    },

    // Поиск по сайту (понадобится для RAG)
    search: {
      provider: 'local'
    },

    logo: '.',
    footer: {
      message: 'Учебный проект по созданию базы знаний',
      copyright: '© 2026 Команда "Нейрослоп"'
    },

    socialLinks: []
  }
})