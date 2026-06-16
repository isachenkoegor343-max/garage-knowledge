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
            { text: 'Обзор подбора', link: '/selection/' },
            { text: 'До 100 000 ₽', link: '/selection/budget-100' },
            { text: '100 000 – 200 000 ₽', link: '/selection/budget-200' },
            { text: '300 000 – 500 000 ₽', link: '/selection/budget-500' },
            { text: '500 000 – 1 000 000 ₽', link: '/selection/budget-1000' }
          ]
        },
        {
          text: ' Проверка и оформление',
          items: [
            { text: 'Выездная диагностика', link: '/selection/inspection' },
            { text: 'Криминалистическая проверка', link: '/selection/legal-check' },
            { text: 'Помощь с документами', link: '/selection/paperwork' },
            { text: 'Автоюридический справочник', link: '/selection/legal-rights' }
          ]
        }
      ],
      '/service/': [
        {
          text: ' Техническая часть',
          items: [
            { text: 'Обзор обслуживания', link: '/service/' },
            { text: 'Устройство автомобиля', link: '/service/device' },
            { text: 'Техобслуживание для новичков', link: '/service/to-basics' }
          ]
        },
        {
          text: ' Календарь и ремонт',
          items: [
            { text: 'Календарь первого года', link: '/service/maintenance-calendar' },
            { text: 'Ремонт своими руками', link: '/service/diy-repair' },
            { text: 'Как не попасть на развод', link: '/service/anti-fraud' }
          ]
        },
        {
          text: ' Полезное',
          items: [
            { text: 'Шиномонтаж и резина', link: '/service/tires' },
            { text: 'Мойка и антикор', link: '/service/washing' }
          ]
        }
      ],
      '/docs/': [
        {
          text: ' Документы и законы',
          items: [
            // { text: 'Обзор документов', link: '/docs/index' },
            { text: 'Регистрация в ГИБДД', link: '/docs/registration' },
            { text: 'ОСАГО и Каско', link: '/docs/insurance' },
            { text: 'Транспортный налог', link: '/docs/tax' }
          ]
        }
      ]
    },

    search: {
      provider: 'local'
    },

    logo: '🚗',
    footer: {
      message: 'Учебный проект по созданию базы знаний',
      copyright: '© 2026 Команда "Нейрослоп"'
    },

    socialLinks: []
  }
})