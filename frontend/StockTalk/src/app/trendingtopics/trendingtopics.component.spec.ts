import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TrendingtopicsComponent } from './trendingtopics.component';

describe('TrendingtopicsComponent', () => {
  let component: TrendingtopicsComponent;
  let fixture: ComponentFixture<TrendingtopicsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TrendingtopicsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TrendingtopicsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
