from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window

# Set a mobile-friendly window size for testing on Windows
Window.size = (360, 640)

class ClickerGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15

        # Game Variables
        self.score = 0
        self.click_power = 1
        self.auto_clicks = 0
        
        self.upgrade_cost = 10
        self.auto_cost = 50

        # UI Elements: Score Display
        self.score_label = Label(
            text="Points: 0", 
            font_size='32sp', 
            bold=True,
            size_hint_y=0.2
        )
        self.add_widget(self.score_label)

        # UI Elements: Main Clicker Button
        self.click_btn = Button(
            text="CLICK ME!", 
            font_size='24sp',
            background_color=(0.2, 0.6, 1, 1),
            size_hint_y=0.4
        )
        self.click_btn.bind(on_press=self.on_click)
        self.add_widget(self.click_btn)

        # UI Elements: Upgrade Click Power Button
        self.upgrade_btn = Button(
            text=f"Upgrade Click (+1)\nCost: {self.upgrade_cost}", 
            font_size='16sp',
            size_hint_y=0.2
        )
        self.upgrade_btn.bind(on_press=self.buy_upgrade)
        self.add_widget(self.upgrade_btn)

        # UI Elements: Buy Auto Clicker Button
        self.auto_btn = Button(
            text=f"Buy Auto-Clicker (+1/s)\nCost: {self.auto_cost}", 
            font_size='16sp',
            size_hint_y=0.2
        )
        self.auto_btn.bind(on_press=self.buy_auto)
        self.add_widget(self.auto_btn)

        # Start the background clock for auto-clicking (runs every 1 second)
        Clock.schedule_interval(self.game_loop, 1.0)

    def update_ui(self):
        """Keep the text on screen up to date."""
        self.score_label.text = f"Points: {self.score}"
        self.upgrade_btn.text = f"Upgrade Click (+1)\nCost: {self.upgrade_cost}"
        self.auto_btn.text = f"Buy Auto-Clicker (+1/s)\nCost: {self.auto_cost}"

    def on_click(self, instance):
        """Triggered when the main button is clicked."""
        self.score += self.click_power
        self.update_ui()

    def buy_upgrade(self, instance):
        """Increase manual click power."""
        if self.score >= self.upgrade_cost:
            self.score -= self.upgrade_cost
            self.click_power += 14354354454354554325352432453253425432532325
            self.upgrade_cost = int(self.upgrade_cost + 0)  # Increase next cost
            self.update_ui()

    def buy_auto(self, instance):
        """Increase passive income."""
        if self.score >= self.auto_cost:
            self.score -= self.auto_cost
            self.auto_clicks += 1
            self.auto_cost = int(self.auto_cost + 0)  # Increase next cost
            self.update_ui()

    def game_loop(self, dt):
        """Passive income generated every second."""
        if self.auto_clicks > 0:
            self.score += self.auto_clicks
            self.update_ui()

class ClickerApp(App):
    def build(self):
        self.title = "Ultimate Clicker"
        return ClickerGame()

if __name__ == '__main__':
    ClickerApp().run()
