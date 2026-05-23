import pygame
import pygame_gui
import GameResource
from pygame_gui.elements import UITextBox,UIButton, UIPanel, UIImage


class Frame:

    def __init__(self, manager, pos, size, bg_color=(50, 50, 50), alpha=255, layer=1,object_id = None, Parent = None):
        self.manager = manager
        self.size = size
        self.bg_rgb = bg_color
        self.alpha = alpha
        self.object_id = object_id
        self.Parent = Parent
        if self.size is not None:
            self.create_panel(pos, self.size, layer)
        else:
            self.panel = None

        
    def create_panel(self, pos, size, layer):
        self.size = size
        
        self.panel = UIPanel(
            relative_rect=pygame.Rect(pos, size),
            starting_height=layer,
            manager=self.manager,
            object_id=self.object_id,
            container=self.Parent,
        )
        
        
        self._apply_background()

    def _apply_background(self):
        if self.panel:
            r, g, b = self.bg_rgb
            
            target_color = pygame.Color(r, g, b, self.alpha)
            
            self.panel.background_colour = target_color
            self.panel.border_colour = pygame.Color(0, 0, 0, 0)
            
            self.panel.rebuild()

    def set_alpha(self, new_alpha):
        self.alpha = max(0, min(255, new_alpha))
        self._apply_background()

    def set_background_color(self, new_bg_color):
        self.bg_rgb = new_bg_color
        self._apply_background()

    def set_position(self, new_pos):
        if self.panel:
            self.panel.set_relative_position(new_pos)

class TextLabel(Frame):

    def __init__(
        self,
        manager,
        text,
        pos,
        size,
        bg_color=(50, 50, 50),
        alpha=255,
        layer=1,
        font_size=4,  
        font_color="#FFFFFF",
        font_name="malgun gothic",
        align_horiz="center",  
        align_vert="center", 
        object_id = None,
        Parent= None,
    ) -> None:
        super().__init__(manager, pos, size, bg_color, alpha, layer,object_id=object_id,Parent=Parent)

        self.current_text = text
        self.font_size = font_size
        self.text_color = font_color
        self.font_name = font_name
        self.align_horiz = align_horiz
        self.align_vert = align_vert  # 'top', 'center', 'bottom'

        # 1. 일단 정렬 없이 UITextBox를 생성합니다.
        self.label = UITextBox(
            html_text=self.get_formatted_text(text),
            relative_rect=pygame.Rect((0,0), self.size),
            manager=self.manager,
            container=self.panel,
            wrap_to_height=False,
            starting_height=layer,
            object_id=object_id,
        )

        # 2. ★ [핵심 꼼수] 생성된 텍스트 박스의 내부 테마 설정을 강제로 변조합니다.
        # 이 방법을 쓰면 외부 테마 JSON 파일 없이 코드 한 줄로 세로 정렬이 먹힙니다!
        
        self.label.text_vert_alignment = self.align_vert
        self.label.text_horiz_alignment = self.align_horiz
        
        # 3. 변경된 세로 정렬 설정을 반영하기 위해 텍스트 박스를 새로고침(Rebuild)합니다.
        self.label.background_colour = pygame.Color(0, 0, 0, 0) # 텍스트 박스 자체의 배경은 100% 투명하게!
        self.label.border_colour = pygame.Color(0, 0, 0, 0)     # 텍스트 박스 자체의 테두리도 투명하게!
        self.label.rebuild()                                    # 적용 후 새로고침

    def get_formatted_text(self, raw_text) -> str:
        """HTML 태그를 이용하여 가로 정렬과 스타일 적용"""
        return (
            f"<div align='{self.align_horiz}'>"
            f"<font face='{self.font_name}' size='{self.font_size}' color='{self.text_color}'>"
            f"{raw_text}"
            f"</font></div>"
        )

    def set_text(self, new_text) -> None:
        self.current_text = new_text
        self.label.set_text(self.get_formatted_text(new_text))
# ==========================================
# [하위 클래스] Frame을 상속받아 이미지를 표시하는 ImageLabel
# ==========================================
class ImageLabel(Frame):

    def __init__(
        self,
        manager,
        image_surface,  # ★ 렌더링할 파이게임 Image Surface 객체
        pos,
        size=None,      # ★ 선택 사항: 지정하지 않으면 이미지 원본 크기를 사용합니다.
        bg_color=(50, 50, 50),
        alpha=0,        # ★ 이미지는 보통 배경 상자가 없어야 하므로 기본 투명도를 0으로 둡니다.
        layer=1,
        object_id = None,
        Parent = None,
    ):
        self.original_image_surface = image_surface
        
        # 1. 크기(size) 인자가 들어오지 않았다면 이미지 원본 크기를 자동으로 계산
        if size is None:
            final_size = image_surface.get_size()
        else:
            final_size = size

        # 2. 계산된 크기로 부모 클래스(Frame) 생성자 호출 -> 베이스 패널 생성
        super().__init__(
            manager=manager,
            pos=pos,
            size=final_size,
            bg_color=bg_color,
            alpha=alpha,
            layer=layer,
            object_id=object_id,
            Parent = Parent,
        )

        # 3. 부모가 생성한 self.panel 위에 실제 pygame_gui.elements.UIImage 배치
        self.image_element = UIImage(
            relative_rect=pygame.Rect((0, 0), self.size),  # 패널 내부 (0,0)에 꽉 차게 배치
            image_surface=self.original_image_surface,
            manager=self.manager,
            container=self.panel,  # 부모의 패널을 컨테이너로 지정
            object_id=object_id,
        )

    def set_image(self, new_image_surface, reset_size=False):
        """표시되는 이미지를 실시간(동적)으로 변경하는 메서드
        :param reset_size: True로 설정 시, 라벨 크기를 새 이미지 크기에 맞춥니다.
        """
        self.original_image_surface = new_image_surface
        self.image_element.set_image(new_image_surface)

        if reset_size:
            # 새 이미지 크기에 맞춰 부모 패널과 이미지 엘리먼트 크기 동시 조절
            new_size = new_image_surface.get_size()
            self.panel.set_dimensions(new_size)
            self.image_element.set_dimensions(new_size)
            self.size = new_size

# ==========================================
# [상위 클래스] 버튼의 기본 기능 및 클릭 이벤트를 관리
# ==========================================
class Button:

    def __init__(self, manager, pos, size, text="", layer=1, object_id=None, Parent= None,):
        """
        :param manager: pygame_gui.UIManager
        :param pos: (x, y) 좌표
        :param size: (width, height) 크기
        :param text: 버튼에 표시할 기본 텍스트 (ImageButton에서는 주로 비워둠)
        :param layer: 레이어 높이 (starting_height)
        :param object_id: 테마 지정을 위한 ID (선택 사항)
        """
        self.Parent = Parent
        self.object_id = object_id
        self.manager = manager
        self.size = size

        # pygame_gui의 UIButton을 생성하여 베이스로 사용합니다.
        self.Frame = Frame(
            manager=self.manager,
            pos=pos, 
            size = size,
            Parent=self.Parent,
            alpha = 0,
            layer=layer,
        )
        # self.Frame.panel.disable()
        
        self.button = UIButton(
            relative_rect=pygame.Rect((0,0), size),
            text=text,
            manager=self.manager,
            starting_height=layer,
            object_id=self.object_id,
            container=self.Frame.panel,
        )

            
    def set_position(self, new_pos):
        """버튼의 위치를 동적으로 변경"""
        self.button.set_relative_position(new_pos)

    def set_text(self, new_text):
        """버튼의 텍스트를 동적으로 변경"""
        self.button.set_text(new_text)
        self.button.rebuild()

    def is_clicked(self, event):
        """
        파이게임 이벤트 루프에서 이 버튼이 클릭되었는지 확인하는 메서드
        :param event: pygame.event.get()에서 꺼내온 이벤트 객체
        :return: 클릭되었다면 True, 아니면 False
        """
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.button:
                return True
        return False

    def disable(self):
        """버튼 비활성화 (클릭 불가능 상태)"""
        self.button.disable()

    def enable(self):
        """버튼 활성화 (클릭 가능 상태)"""
        self.button.enable()


# ==========================================
# [하위 클래스 1] 텍스트 스타일과 정렬을 강화한 TextButton
# ==========================================
class TextButton(Button):  # 베이스는 클릭 감지가 가능한 Button

    def __init__(
        self,
        manager,
        text,
        pos,
        size,
        bg_color=(50, 50, 50),
        alpha=255,
        layer=1,
        font_size=4,  
        font_color="#FFFFFF",
        font_name="malgun gothic",
        align_horiz="center",  
        align_vert="center", 
        object_id=None,
        Parent= None,
    ) -> None:
        
        super().__init__(
            manager=manager,
            pos=pos,
            size=size,
            text="", 
            layer=layer+1,
            object_id=object_id,
            Parent = Parent,
        )

        self.label_component = TextLabel(
            manager=manager,
            text=text,
            pos=(0,0),         
            size=size,         
            bg_color=bg_color,
            alpha=alpha,
            layer=layer,    
            font_size=font_size,
            font_color=font_color,
            font_name=font_name,
            align_horiz=align_horiz,
            align_vert=align_vert,
            object_id=object_id,
            Parent = self.Frame.panel,
        )
        self.label_component.label.disable()
        self.label_component.panel.disable()


    def change_text(self, new_text) -> None:
        """우리가 만든 TextLabel의 set_text를 호출하여 텍스트 변경"""
        self.label_component.set_text(new_text)

    def set_position(self, new_pos):
        """버튼의 위치를 이동할 때"""
        super().set_position(new_pos)
        


class ImageButton(Button):

    def __init__(
        self,
        manager,
        pos,
        normal_image,  
        hovered_image=None,  
        selected_image=None,  
        size=None,  #
        layer=1,
        object_id = None,
        Parent= None,
    ):
        if size is None:
            final_size = normal_image.get_size()
        else:
            final_size = size

        super().__init__(
            manager=manager, pos=pos, size=final_size, text="", layer=layer, object_id=object_id, Parent=Parent
        )

        self.button.normal_images = normal_image
        self.button.set_image(normal_image)
        
        

        if hovered_image:
            self.button.hovered_images = hovered_image
        else:
            self.button.hovered_images = normal_image
        
        if selected_image:
            self.button.selected_images = selected_image
        else:
            self.button.selected_images = normal_image