import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewSavedPostsComponent } from './view-saved-posts.component';

describe('ViewSavedPostsComponent', () => {
  let component: ViewSavedPostsComponent;
  let fixture: ComponentFixture<ViewSavedPostsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ViewSavedPostsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ViewSavedPostsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
